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
        scanf("%d", &temp1);
        if (((temp1 <= 0) | (temp1 >= 30))|(temp>temp1))
            return 0;
        Marr[i] = temp1;
    }
    //Marr 는 공간 절약을 위해 개수를 저장하던 임무를 다하면 
    //바로 result 값이 들어가 result[n] 의 역할을 수행.
    for(int i=0;i<n;i++)
    {
        int temp=Marr[i]-Narr[i]+1;
        int result=0;
        for(int j=1;j<temp+1;j++)
        {
            result += addall(j);
        }
        Marr[i]=result;
    }
    for(int i=0;i<n;i++)
    {
        printf("%d\n",Marr[i]);
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

지금 개수 세는 방식이 잘못됬음 다시 수정필요.
1 4
2 3

12-54321
23-4321
34-321
45-21
56-1
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
