import java.util.*;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        String[] answer = {};
        HashMap<String,Integer> MapByName = new HashMap<String,Integer>();
        HashMap<Integer,String> MapByRate = new HashMap<Integer,String>();
        for(int i=0;i<players.length;i++){
            MapByName.put(players[i],i+1);
            MapByRate.put(i+1,players[i]);
        }
        for(int i=0;i<callings.length;i++){
            String N1 = callings[i];
            int R1 = MapByName.get(N1);
            int R2 = R1-1;
            String N2 = MapByRate.get(R2);
            MapByName.put(N1,R2);
            MapByName.put(N2,R1);
            MapByRate.put(R2,N1);
            MapByRate.put(R1,N2);
        }
        answer = MapByRate.values().toArray(new String[MapByRate.size()]);
        return answer;
    }
}