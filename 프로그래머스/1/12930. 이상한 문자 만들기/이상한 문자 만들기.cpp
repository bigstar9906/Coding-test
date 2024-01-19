#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    int count = 1;
    for(int i=0;i<s.length();i++){
        if(s[i]==' '){
            count = 0;    
        }
        else if(count%2==1) s[i] = toupper(s[i]);
        else s[i] = tolower(s[i]);
        count++;
    }
    
    return s;
}