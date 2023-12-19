class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = health;
        int index = 0;
        int band_cnt = 0;
        for(int i=attacks[0][0];i<=attacks[attacks.length-1][0];i++){
            if(i==attacks[index][0]){
                band_cnt=0;
                answer-=attacks[index][1];
                index++;
                if(answer<1) return -1;
            } else{
                if(answer<health){
                    answer+=bandage[1];
                    band_cnt +=1;
                    if(band_cnt==bandage[0]){
                        band_cnt =0;
                        answer+=bandage[2];
                    }
                    if(answer>health) answer=health;
                }
                
            }
        }
        return answer;
    }
    
    
}