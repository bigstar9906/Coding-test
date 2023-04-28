import java.util.HashMap;
import java.util.List;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        
        int[] answer = new int[photo.length];
        HashMap<String,Integer> MapByYearning = new HashMap<String,Integer>();
        for(int i=0;i<name.length;i++){
            MapByYearning.put(name[i],yearning[i]);
        }
        for(int i=0;i<photo.length;i++){
            int sum = 0;
            for(int j=0;j<photo[i].length;j++){
                if(MapByYearning.containsKey(photo[i][j])){
                    sum+= MapByYearning.get(photo[i][j]);
                }                
            }
            answer[i] = sum;
        }
        return answer;
    }
}