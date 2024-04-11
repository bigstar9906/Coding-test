import java.util.ArrayList;
class Solution {
    public ArrayList<Integer> solution(int[] answers) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        int[] f = {1,2,3,4,5};
        int[] s = {2,1,2,3,2,4,2,5};
        int[] t = {3,3,1,1,2,2,4,4,5,5};
        int[] points = {0,0,0};
        int ans = 0;
        for( int i=0;i<answers.length;i++){
            ans = answers[i];
            if(ans==f[i%5]){
                points[0]+=1;
            }
            if(ans==s[i%8]){
                points[1]+=1;
            }
            if(ans==t[i%10]){
                points[2]+=1;
            }
        }
        int max = 0;
        for(int i=0;i<points.length;i++){
            if(points[i]>max){
                answer = new ArrayList<Integer>();
                max = points[i];
                answer.add(i+1);
            }else if(points[i]==max){
                answer.add(i+1);
            }
        }
        return answer;
        
    }
}