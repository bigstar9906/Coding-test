#include<iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

int solution(vector<string> friends, vector<string> gifts) {
    vector<int> answer = {};
    vector<int> gift_point = {};
    vector<vector<int>> give_take;
    for(int i=0;i<friends.size();i++){
        gift_point.push_back(0);
        vector<int> temp  ={};
        for(int j=0;j<friends.size();j++){
            temp.push_back(0);
        }
        give_take.push_back(temp);
    }
    for(int i=0;i<gifts.size();i++){
        vector<string> split;
        int space = find(gifts[i].begin(),gifts[i].end(),' ')-gifts[i].begin();
        split.push_back(gifts[i].substr(0,space));
        split.push_back(gifts[i].substr(space+1));
        int giver =find(friends.begin(),friends.end(),split[0])-friends.begin();
        int reciever =find(friends.begin(),friends.end(),split[1])-friends.begin();
        give_take[giver][reciever] +=1;
        give_take[reciever][giver] -=1;
        gift_point[giver]+=1;
        gift_point[reciever]-=1;
    }
    for(int i=0;i<friends.size();i++){
        int gift = 0;
        for(int j=0;j<friends.size();j++){
            if(give_take[i][j]>0) gift++;
            else if (give_take[i][j]==0&&gift_point[i]>gift_point[j])gift++;
        }
        answer.push_back(gift);
    }
    return *max_element(answer.begin(),answer.end());
}