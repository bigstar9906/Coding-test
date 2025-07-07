import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> hashMap = new HashMap<>();
        for(int i=0;i<participant.length;i++){
            String current = new String(participant[i]);
            if(hashMap.containsKey(current)){
                hashMap.put(current,hashMap.get(current)+1);
            }else{
                hashMap.put(current,1);
            }
        }
        for(int i=0;i<completion.length;i++){
            String current = new String(completion[i]);
            hashMap.put(current,hashMap.get(current)-1);
            if(hashMap.get(current)==0){
                hashMap.remove(current);
            }
        }
        for(String key : hashMap.keySet()){
            return key;
        }
        return "";
    }
}