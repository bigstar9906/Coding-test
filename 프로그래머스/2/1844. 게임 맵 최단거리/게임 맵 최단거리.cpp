#include<vector>
#include<deque>
#include<tuple>
using namespace std;

struct node {
    vector<int> position;
    int step;
    int previous; //2 위 3 오른쪽 5 왼쪽 7 아래
};

int solution(vector<vector<int> > maps)
{
    int answer = -1;
    vector<int> position = {0,0};
    deque<node> stack;
    stack.push_back({position,1,1});
    int n = maps.size()-1;
    int m = maps[0].size()-1;
    int x,y;
    node current;
    while(stack.size()>0){// n,m에 도착 시 or 갈 곳이 없을 때
        current = stack[0];
        stack.pop_front();
        position = current.position;
        int can_go = 1;
        x = position[1];
        y = position[0];
        int step = current.step;
        if(step==1) maps[0][0] = -1;
        if(((x==m)&&(y==n-1))||((x==m-1)&&(y==n))) return step+1;
        // position 기준 네 방향 1인 블럭 스택에 넣고 값 변경
        if(x<m&&current.previous%3!=0){// 나누기를 통해 이전에 탐색한 방향은 판단x
            if(maps[y][x+1]==1){
                stack.push_back({{y,x+1},step+1,5});
                maps[y][x+1] = step+1;                
                can_go*=3;
            }
        }
        if(y<n&&current.previous%7!=0){
            if(maps[y+1][x]==1){
                can_go*=7;
                int prev = 2;
                if(can_go%3==0) prev*=3;
                stack.push_back({{y+1,x},step+1,prev});
                maps[y+1][x]=step+1;
            }
        }
        if(y>0&&current.previous%2!=0){
            if(maps[y-1][x]==1){
                int prev = 7;
                can_go*=2;
                if(can_go%3==0)prev*=3;
                stack.push_back({{y-1,x},step+1,prev});
                maps[y-1][x] = step+1;
            }
        }
        if(x>0&&current.previous%5!=0){
            if(maps[y][x-1]==1){
                int prev = 3;
                if(can_go%2==0)prev*2;
                if(can_go%7==0)prev*7;
                stack.push_back({{y,x-1},step+1,prev});
                maps[y][x-1]=step+1;
            }
        }
        
    }
    return answer;
}