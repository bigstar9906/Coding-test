#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

unsigned long long Combine(int,int);
unsigned long long facto(int,int);
int bigger (int, int);
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
        scanf("%d", &temp1);
        if (((temp1 <= 0) | (temp1 >= 30))|(temp>temp1))
            return 0;
        Marr[i] = temp1;
    }
    
    for(int i=0;i<n;i++)
    {
    printf("%llu\n",Combine(Marr[i],Narr[i]));        
    }
    
    free(Narr);
    free(Marr);
    return 0;
}


int bigger (int x, int y)
{
    if(x>=y) return x;
    else return y;
}

unsigned long long Combine(int x,int y)
{
    int temp = bigger(y,x-y);
    int temp1;
    if (temp == y) temp1 = x-y;
    else temp1 = y;
    return facto(x,temp)/facto(temp1,0);
}

unsigned long long facto(int x,int y)
{
    if((x==1)|x==0)return 1;
    if(x==y) return 1;
    return (x*facto(x-1,y));
}
