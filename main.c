#include <string.h>  /* strcpy */
#include <stdlib.h>  /* malloc */
#include <stdio.h>   /* printf */
#include "uthash.h"
#include "parameters.h"
#include "keywords.h"

#define keywordLen 20 //最长关键词长度
#define keywordNum 201 //关键词个数
//const char *keywordsList[]={ "==", "=", "!=", ";" };
//const float weight1[keywordNum]={-0.6,0.1,0.3,0.5};
//const float weight2[][keywordNum]={{1.0,2.0,2.5,0.4},{-0.5,-0.9,0.0,-0.2}};
//const float bias2[]={-0.5,1.0};

struct custom_set {
    char name[keywordLen];             /* key (string is WITHIN the structure) */
    int id;
    UT_hash_handle hh;         /* makes this structure hashable */
};

void count_keyword_frequency(const char *input, struct custom_set *keywords, float *freq){
    //write frequencies into 'freq'
    int n=strlen(input);
    //static float freq[keywordNum]={0.0};
    int *inkeywords=(int *)malloc(n*sizeof(int));
    for(int i=0;i<n;i++){
        inkeywords[i]=0;
    }
    for(int l=keywordLen;l>=1;l--){
        for(int i=0;i<=n-l;i++){
            int flag=0;
            char substr[keywordLen+1]; //substr=input[i:i+l]
            for(int j=0;j<=l-1;j++){
                if(inkeywords[i+j]==1){
                    flag=1;
                    break;
                }
                substr[j]=input[i+j];
            }
            if(flag==1){
                continue;
            }
            substr[i+l]='\0';
            struct custom_set *s=NULL;
            HASH_FIND_STR(keywords, substr, s);
            if(s){
                for(int j=0;j<=l-1;j++){
                    inkeywords[i+j]=1;
                }
                freq[s->id]=freq[s->id]+1.0;
            }
        }
    }
    free(inkeywords);
    for(int i=0;i<keywordNum;i++){
        freq[i]=freq[i]/n;
    }
}

float blas1(const float *w, float *x, float b, int n){
    //return w'*x+b
    float ans=b;
    for(int i=0;i<n;i++){
        ans=ans+w[i]*x[i];
    }
    return ans;
}

void blas2(const float *W,float *x,const float *b,int m,int n,float *ans){
    //write W*x+b into ans
    for(int i=0;i<m;i++){
        ans[i]=b[i];
        for(int j=0;j<n;j++){
            ans[i]=ans[i]+W[i*n+j]*x[j];
        }
    }
}

int main(int argc, char *argv[]) {
    //const char *names[] = { "joe", "bob", "betty", NULL };
    struct custom_set *s, *tmp, *keywords = NULL;
    for (int i = 0; i<keywordNum; i++) {
        s = (struct custom_set *)malloc(sizeof *s);
        strcpy(s->name, keywordsList[i]);
        s->id = i;
        HASH_ADD_STR(keywords, name, s);
    }

    const char *input1="int i = 0;, http://";
    const char *input2="Here is an example of text.";

    float freq[keywordNum]={0.0};
    count_keyword_frequency(input1,keywords,freq);
    //count_keyword_frequency(input2,keywords,freq);

    for(int i=0;i<sizeof(freq)/sizeof(freq[0]);i++){
        if (freq[i]>0)
            printf("%f  ", freq[i]);
    }
    printf("\n");

    float ans1[sizeof(bias1)/sizeof(bias1[0])]={0.0};
    blas2(&weight1[0][0],freq,bias1,sizeof(bias1)/sizeof(bias1[0]),keywordNum,ans1);

    float ans2[sizeof(bias2)/sizeof(bias2[0])]={0.0};
    blas2(&weight2[0][0],ans1,bias2,sizeof(bias2)/sizeof(bias2[0]),keywordNum,ans2);

    for(int i=0;i<sizeof(bias2)/sizeof(bias2[0]);i++){
        printf("%f\n", ans2[i]);
    }

    HASH_FIND_STR(keywords, ";", s);
    if (s) printf(";'s id is %d\n", s->id);

    /* free the hash table contents
    HASH_ITER(hh, keywords, s, tmp) {
      HASH_DEL(keywords, s);
      free(s);
    }
    */
    return 0;
}