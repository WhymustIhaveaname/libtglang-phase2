#include <string.h>  /* strcpy */
#include <stdlib.h>  /* malloc */
#include <stdio.h>   /* printf */
#include "uthash.h"

#define keywordLeng 25 //最长关键词长度
#define keywordNum 100 //关键词个数

struct custom_set {
    char name[keywordLeng];             /* key (string is WITHIN the structure) */
    int id;
    UT_hash_handle hh;         /* makes this structure hashable */
};

float *count_keyword_frequency(const char *input, struct custom_set *keywords){
    //This function can only be used once, because freq will only be initialized once.
    int n=strlen(input);
    static float freq[keywordNum]={0.0};
    int *inkeywords=(int *)malloc(n*sizeof(int));
    for(int i=0;i<n;i++){
        inkeywords[i]=0;
    }
    for(int l=keywordLeng;l>=1;l--){
        for(int i=0;i<=n-l;i++){
            int flag=0;
            char substr[keywordLeng+1]; //substr=input[i:i+l]
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
            struct custom_set *s;
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
    return freq;
}

int main(int argc, char *argv[]) {
    //const char *names[] = { "joe", "bob", "betty", NULL };
    const char *keywordsList[]={ "==", "=", "!=", ";",NULL };
    struct custom_set *s, *tmp, *keywords = NULL;
    for (int i = 0; keywordsList[i]; ++i) {
        s = (struct custom_set *)malloc(sizeof *s);
        strcpy(s->name, keywordsList[i]);
        s->id = i;
        HASH_ADD_STR(keywords, name, s);
    }

    const char *input1="Here = an example of code;;";
    const char *input2="Here is an example of text.";

    float *freq1=count_keyword_frequency(input1,keywords);
    //float *freq2=count_keyword_frequency(input2,keywords);

    for(int i=0;i<=6;i++){
        printf("%f\n", freq1[i]);
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