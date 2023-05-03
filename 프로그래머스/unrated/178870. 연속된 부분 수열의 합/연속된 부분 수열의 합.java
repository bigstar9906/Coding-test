class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = new int[]{0,999999};
        int start_index = 0;
        int end_index = 0;
        int current = 0;
        for(;end_index<sequence.length;end_index++){
            current +=sequence[end_index];
            if(current>k){
                current-=(sequence[start_index]+sequence[end_index]);
                start_index+=1;
                end_index-=1;
            }else if(current==k&&answer[1]-answer[0]>end_index-start_index){
                answer[0] = start_index;
                answer[1] = end_index;
            }
        }
        return answer;
        }
}