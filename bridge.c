#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int Combine(int,int);
int facto(int);

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
    //Marr 는 공간 절약을 위해 개수를 저장하던 임무를 다하면 
    //바로 result 값이 들어가 result[n] 의 역할을 수행.
    
    for(int i=0;i<n;i++)
    {
    printf("\n\n%d,%d\n",Marr[i],Narr[i]);
    printf("%d\n",Combine(Marr[i],Narr[i]));        
    }
    
    free(Narr);
    free(Marr);
    return 0;
}

int facto(int x)
{
    if((x==1)|x==0)return 1;
    return x*facto(x-1);
}


int Combine(int x,int y)
{
    return (facto(x)/facto(y))/facto(x-y);
}
