#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int addall(int,int);

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
        
        //combine return
    }
    for(int i=0;i<n;i++)
    {
        printf("%d\n",Marr[i]);
    }
    free(Narr);
    free(Marr);
    return 0;
}


int Combine(int x,int y)
{
    int temp;
    return 0;
}
