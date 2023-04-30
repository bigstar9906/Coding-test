import java.util.Arrays;
import java.util.Comparator;
class Solution {
    public int solution(int[][] targets) {
        int answer=0;
        boolean separated = false;
        int current_endPoint = 0;
        targets = sortOfEndPoint(targets);//Endpoint로 정렬
        for(int i=0;i<targets.length;i++){
            if(current_endPoint<=targets[i][0]){
                answer+=1;
                current_endPoint = targets[i][1];
            }
        }
        
        return answer;
    }
    
    public static int[][] sortOfEndPoint(int[][] targets){
        Arrays.sort(targets, new Comparator<int[]>(){
            public int compare(int[] o1, int[] o2){
                return o1[1]-o2[1];
            }
        });
        return targets;
    }
}