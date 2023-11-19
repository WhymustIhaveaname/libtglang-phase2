#include <string.h>  /* strcpy */
#include <stdlib.h>  /* malloc */
#include <stdio.h>   /* printf */
#include "uthash.h"
#include "tglang.h"
#include "parameters.h"

#define KEYWORDLEN 25 //最长关键词长度
#define KEYWORDNUM 4  //关键词个数
const char *keywords_list[]={ "==", "=", "!=", ";" };
const float weight3[KEYWORDNUM]={-0.6,0.1,0.3,0.5};
const float weight4[][KEYWORDNUM]={{1.0,2.0,2.5,0.4},{-0.5,-0.9,0.0,-0.2}};
const float bias4[]={-0.5,1.0};

struct hash_set {
    char name[KEYWORDLEN];     /* key (string is WITHIN the structure) */
    int id;
    UT_hash_handle hh;         /* makes this structure hashable */
};

void count_keyword_frequency(const char *input, struct hash_set *keywords, float *freq){
    /*
        count the appearence of keywords in input and write the result into freq
    */
    int n=strlen(input);
    char *inkeywords=(char *)calloc(n,sizeof(char));
    for(int l=KEYWORDLEN;l>0;l--){
        for(int i=0;i<=n-l;i++){
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
    //return w'*x+b
    //n=len(w)=len(x)
    float ans=b;
    for(int i=0;i<n;i++){
        ans=ans+w[i]*x[i];
    }
    return ans;
}

void blas2(const float *W,float *x,const float *b,int m,int n,float *ans){
    /* write W*x+b into ans
    m=len(W)=len(b)=len(ans), n=len(W[0])=len(x)
    float ans1[sizeof(bias1)/sizeof(bias1[0])]={0.0};
    blas2(&weight1[0][0],freq,bias1,sizeof(bias1)/sizeof(bias1[0]),sizeof(freq)/sizeof(freq[0]),ans1);
    */
    for(int i=0;i<m;i++){
        ans[i]=b[i];
        for(int j=0;j<n;j++){
            ans[i]=ans[i]+W[i*n+j]*x[j];
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

void print_hash_set(struct hash_set *keywords){
    struct hash_set *s;
    printf("keywords: ");
    for(s=keywords; s != NULL; s=s->hh.next) {
        printf("%s(%d), ",s->name,s->id);
    }
    printf("\n");
}

enum TglangLanguage tglang_detect_programming_language(const char *text) {
    struct hash_set *s, *keywords = NULL;
    for (int i = 0; i<KEYWORDNUM; i++) {
        s = (struct hash_set *)malloc(sizeof *s);
        strcpy(s->name, keywords_list[i]);
        s->id = i;
        HASH_ADD_STR(keywords, name, s);
    }
    print_hash_set(keywords);

    while (text[0] == '\n' || text[0] == ' ') { // text = text.strip()
        text++;
    }

    float freq[KEYWORDNUM]={0.0};
    count_keyword_frequency(text,keywords,freq);

    printf("keyword freq in %s: ",text);
    for(int i=0;i<KEYWORDNUM;i++){
        printf("%.4f, ", freq[i]);
    }
    printf("\n");

    float ans1[sizeof(bias1)/sizeof(bias1[0])]={0.0};
    blas2((const float *)weight1,freq,bias1,sizeof(bias1)/sizeof(bias1[0]),sizeof(freq)/sizeof(freq[0]),ans1);
    relu(ans1,sizeof(bias1)/sizeof(bias1[0]));

    float ans2[sizeof(bias2)/sizeof(bias2[0])]={0.0};
    blas2((const float *)weight2,ans1,bias2,sizeof(bias2)/sizeof(bias2[0]),sizeof(ans1)/sizeof(ans1[0]),ans2);

    for(int i=0;i<sizeof(bias2)/sizeof(bias2[0]);i++){
        printf("%f\n", ans2[i]);
    }
    // printf("%f\n", ans1);

    // float ans2[2]={0.0};
    // blas2(weight2,freq,bias2,sizeof(bias2)/sizeof(bias2[0]),KEYWORDNUM,ans2);
    // printf("%f\n", ans2[1]);
    return TGLANG_LANGUAGE_OTHER;
}

int main(int argc, char *argv[]) {
    const char *input1="Here == = != === an example of code;";
    const char *input2="Here is an example of text.";

    tglang_detect_programming_language(input1);

    // /* free the hash table contents
    // HASH_ITER(hh, keywords, s, tmp) {
    //   HASH_DEL(keywords, s);
    //   free(s);
    // }*/
    return 0;
}