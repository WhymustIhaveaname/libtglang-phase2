#include <string.h>  /* strcpy */
#include <stdlib.h>  /* malloc */
#include <stdio.h>   /* printf */
#include "uthash.h"

const int maxKeywordLength=25;

struct my_struct {
    char name[25];             /* key (string is WITHIN the structure) */
    int id;
    UT_hash_handle hh;         /* makes this structure hashable */
};


int main(int argc, char *argv[]) {
    //const char *names[] = { "joe", "bob", "betty", NULL };
    const char *keywordsList[]={ "=", "==", "!=", NULL };
 
    struct my_struct *s, *tmp, *keywords = NULL;

    for (int i = 0; keywordsList[i]; ++i) {
        s = (struct my_struct *)malloc(sizeof *s);
        strcpy(s->name, keywordsList[i]);
        s->id = i;
        HASH_ADD_STR(keywords, name, s);
    }

    HASH_FIND_STR(keywords, "!=", s);
    if (s) printf("betty's id is %d\n", s->id);

    /* free the hash table contents
    HASH_ITER(hh, users, s, tmp) {
      HASH_DEL(users, s);
      free(s);
    }
    */
    return 0;
}