#include <string>
#include <vector>
#include <deque>

using namespace std;

int solution(vector<int> numbers, int target) {
    int answer = 0;
    deque<int> queue;
    int index = 1;
    queue.push_front(target);
    while(numbers.size()>0){
        int number = numbers.back();
        numbers.pop_back();
        bool isEnd = (numbers.size()==0);
        for(int i=0;i<index;i++){
            int node = queue[0];
            queue.pop_front();
            if(isEnd)
            {
                if(node-number==0)answer++;
                if(node+number==0)answer++;
            }
            else{
            queue.push_back(node-number);
            queue.push_back(node+number);
            }
        }
        index*=2;        
    }
    
    return answer;
}