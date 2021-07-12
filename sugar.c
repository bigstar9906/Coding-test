#include <stdio.h>

int main()
{
    int n = 0;
   scanf("%d",&n);
   if((n<3)|(n>5000)) return 0;
   int result=-1;
   for (int i =n/5; i>-1;i--)
   {
       if((n-5*i)%3==0) 
       {
           result = i+(n-5*i)/3;
           break;
       }
        else result =-1;
       
   }
   printf("%d",result);
   return 0;
}
