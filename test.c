#include<stdio.h>

int Combine(int,int);
unsigned long long facto(unsigned long long,int);

int main(void)
{
    printf("%llu",facto(29,15)/facto(14,0));
    return 0;
}

unsigned long long facto(unsigned long long x,int y)
{
    if((x==1)|x==0)return 1;
    if(x==y) return 1;
    return (x*facto(x-1,y));
}

/*int Combine(int x,int y)
{
    return (facto(x)/facto(y))/facto(x-y);
}*/
