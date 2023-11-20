#include <string.h>  /* strcpy */
#include <stdlib.h>  /* malloc */
#include <stdio.h>   /* printf */
#include "uthash.h"
#include "tglang.h"
#include "parameters.h"
// parameters.h contains
// #define KEYWORDLEN 25
// #define KEYWORDNUM 4
// const char *keywords_list[]={ "==", "=", "!=", ";" };
// const float weight[][KEYWORDNUM]={{0.0,0.0,0.0,0.0},{1.0,0.5,1.0,0.2}};
// const float bias[]={0.9,0.0};

#define STRHARDCUT 512

struct hash_set {
    char name[KEYWORDLEN+1];     /* key (string is WITHIN the structure) */
    int id;
    UT_hash_handle hh;         /* makes this structure hashable */
};

/* free the hash table contents
HASH_ITER(hh, keywords, s, tmp) {
  HASH_DEL(keywords, s);
  free(s);
}*/

void print_hash_set(struct hash_set *keywords){
    struct hash_set *s;
    printf("keywords: ");
    for(s=keywords; s != NULL; s=s->hh.next) {
        printf("%s(%d), ",s->name,s->id);
    }
    printf("\n");
}

void count_keyword_frequency(const char *input, struct hash_set *keywords, float *freq){
    /*
        count the appearence of keywords in input and write the result into freq
    */
    int n = strlen(input);
    n = n < STRHARDCUT ? n : STRHARDCUT;
    char *inkeywords=(char *)calloc(n,sizeof(char));
    for(int l=KEYWORDLEN;l>0;l--){
        for(int i=0;i<=n-l;i++){
            while(inkeywords[i]==1){
                i++;
            }
            int flag=-1;
            char substr[KEYWORDLEN+1]={'\0'}; //substr=input[i:i+l]
            for(int j=0;j<l;j++){
                if(inkeywords[i+j]==1){
                    flag=j;
                    break;
                }
                substr[j]=input[i+j];
            }
            if(flag>=0){
                i += flag;
                continue;
            }

            struct hash_set *s=NULL;
            HASH_FIND_STR(keywords, substr, s);
            if(s){
                for(int j=0;j<l;j++){inkeywords[i+j]=1;}
                freq[s->id]=freq[s->id]+1.0;
            }
        }
    }
    free(inkeywords);
    // for(int i=0;i<KEYWORDNUM;i++){
    //     freq[i]=freq[i]/n;
    // }
}

float blas1(const float *w, float *x, float b, int n){
    /*
        return w'*x+b
        n=len(w)=len(x)
    */
    float ans = b;
    for(int i=0;i<n;i++){
        ans += w[i]*x[i];
    }
    return ans;
}

void blas2(const float *W,float *x,const float *b,int m,int n,float *ans){
    /*
        write W*x+b into ans
        m=len(W)=len(b)=len(ans), n=len(W[0])=len(x)
        e.g.
        float ans1[sizeof(bias1)/sizeof(bias1[0])]={0.0};
        blas2(&weight1[0][0],freq,bias1,sizeof(bias1)/sizeof(bias1[0]),sizeof(freq)/sizeof(freq[0]),ans1);
    */
    for(int i=0;i<m;i++){
        ans[i] = b[i];
        for(int j=0;j<n;j++){
            ans[i] += W[i*n+j]*x[j];
        }
    }
}

void relu(float *x, int n){
    for(int i=0;i<n;i++){
        if(x[i]<0.0){
            x[i]=0.0;
        }
    }
}

enum TglangLanguage fc_classify(const char *text) {
    struct hash_set *s, *tmp, *keywords = NULL;
    for (int i = 0; i<KEYWORDNUM; i++) {
        s = (struct hash_set *)malloc(sizeof *s);
        strcpy(s->name, keywords_list[i]);
        s->id = i;
        HASH_ADD_STR(keywords, name, s);
    }
    //print_hash_set(keywords);

    while (text[0] == '\n' || text[0] == ' ') { // text = text.strip()
        text++;
    }

    float freq[KEYWORDNUM]={0.0};
    count_keyword_frequency(text,keywords,freq);
    // printf("nz freq: ");
    // for(int i=0;i<KEYWORDNUM;i++){
    //     if(freq[i]>0){printf("%.1f %s, ", freq[i],keywords_list[i]);}
    // }
    // printf("\n");

    {
        float ans1[net1_HIDDENSIZE],ans2[2];
        blas2((const float *)net1_wt1,freq,net1_b1,net1_HIDDENSIZE,KEYWORDNUM,ans1);
        relu(ans1,net1_HIDDENSIZE);
        blas2((const float *)net1_wt2,ans1,net1_b2,2,net1_HIDDENSIZE,ans2);

        // printf("0/1 classify ans: %.2f, %.2f\n",ans2[0],ans2[1]);

        if(ans2[0]>ans2[1]){
            // free the hash table contents
            HASH_ITER(hh, keywords, s, tmp) {
                HASH_DEL(keywords, s);
                free(s);
            }
            return TGLANG_LANGUAGE_OTHER;
        }
    }
    
    float bns1[net2_HIDDENSIZE],bns2[28];
    blas2((const float *)net2_wt1,freq,net2_b1,net2_HIDDENSIZE,KEYWORDNUM,bns1);
    relu(bns1,net2_HIDDENSIZE);
    blas2((const float *)net2_wt2,bns1,net2_b2,28,net2_HIDDENSIZE,bns2);

    int maxidx = 0;
    float maxval = bns2[0];
    for(int i=1;i<28;i++){
        if(bns2[i]>maxval){
            maxval = bns2[i];
            maxidx = i;
        }
    }
    // free the hash table contents
    HASH_ITER(hh, keywords, s, tmp) {
        HASH_DEL(keywords, s);
        free(s);
    }
    return (enum TglangLanguage) maxidx+1;
}

enum TglangLanguage tglang_detect_programming_language(const char *text) {
    return fc_classify(text);
}

int main(int argc, char *argv[]) {
    int keyword_num = sizeof(keywords_list) / sizeof(keywords_list[0]);
    printf("There are %d keywords\n", keyword_num);
    
    printf("reading %s",argv[1]);
    FILE *in = fopen(argv[1], "rb");
    if (in == NULL) {
        fprintf(stderr, "Failed to open input file %s\n", argv[1]);
        return 1;
    }
    fseek(in, 0, SEEK_END);
    long fsize = ftell(in);
    fseek(in, 0, SEEK_SET);
    char *text = malloc(fsize + 1);
    fread(text, fsize, 1, in);
    fclose(in);
    printf("5\n");
    text[fsize] = 0;
    printf("text len: %ld\n",fsize);
    
    enum TglangLanguage type = tglang_detect_programming_language(text);
    printf("classified as %d\n",type);

    return 0;
}