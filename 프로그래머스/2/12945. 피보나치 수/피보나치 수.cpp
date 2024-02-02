#include <string>
#include <vector>

using namespace std;



int solution(int n) {
    vector<int> fibo = {0,1};
    for(int i=1;i<n;i++){
        int result = fibo[i-1]+fibo[i];
        if(result>1234567) result %=1234567;
        fibo.push_back(result);
    }
    return fibo[n];
}