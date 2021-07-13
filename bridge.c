#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int addall(int);

int main(void)
{
 int n;
 int* Narr;
 int* Marr;
 scanf("%d",&n);
 Narr = (int *)malloc(sizeof(int)*n);
 Marr = (int *)malloc(sizeof(int)*n);
 char s1[3];
 for(int i=0; i<n;i++)
    {
        int temp,temp1;
        scanf("%d",&temp);
        if((temp<=0)|(temp>=30)) return 0;
        Narr[i]=temp;
        scanf("%d", &temp);
        if (((temp <= 0) | (temp >= 30))|(temp>temp1))
            return 0;
        Marr[i] = temp;
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<)
    }
    
    free(Narr);
    free(Marr);
    return 0;
}


int addall(int x)
{
    return (x+1)*x*0.5;
}

/*
ㄱ 1
ㄴ 2
ㄷ 3 
ㄹ 
123 - 4
124 - 3
125 - 2
126 - 1
134 - 3
135 - 2
136 - 1
145 -2
146 -1
156 -1
234 - 3
235 - 2
236 - 1
245 -2
246 -1
256 -1
345 -2
346 -1
356 -1
456 -1
*/
