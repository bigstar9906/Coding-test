#include <string>
#include <vector>

using namespace std;

int solution(int n, vector<vector<int>> computers) {
    int answer =0;
    vector<int> connected;
    vector<int> disconnected;
    vector<int> next_con;
    bool first = true;
    for(int i=1;i<n;i++){
        int node = computers[0][i];
        if(node==0) disconnected.push_back(i);
        else connected.push_back(i);
    }
    if(disconnected.size()== 0) return 1;
    while(disconnected.size()>0)
    {
    if(!first){
        vector<int> roots = disconnected;
        int root = roots[0];
        connected = {};
        disconnected = {};
        for(int i=1;i<roots.size();i++){
            computers[root][roots[i]]==0?disconnected.push_back(roots[i]):connected.push_back(roots[i]);
        }
    }
    first = false;
    while(connected.size()>0){
        for(int i=0;i<connected.size();i++){
            for(int j=0;j<disconnected.size();j++){
                if(computers[connected[i]][disconnected[j]]==1){
                    next_con.push_back(disconnected[j]);
                    disconnected.erase(disconnected.begin()+j);
                    j--;
                }
            }
        }
        connected = next_con;
        next_con = {};
    }
        answer++;
    }
    
    return answer;
}