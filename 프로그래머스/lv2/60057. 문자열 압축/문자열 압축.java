class Solution {
    public int solution(String s) {
        int answer = s.length();
        for(int duplicate_digit = 1;duplicate_digit<=s.length()/2;duplicate_digit++)
        {
            int duplicate_cnt = 0;
            int continuity=0;
            for(int index = 0;index+2*duplicate_digit<=s.length();)
            {
               if(s.substring(index,index+duplicate_digit).equals(s.substring(index+duplicate_digit,index+2*duplicate_digit)))
               {
                   continuity+=1;
               }
                else{
                    if(continuity!=0)duplicate_cnt += duplicate_digit*continuity-Integer.toString(continuity+1).length();
                    continuity = 0;
                }
                index+=duplicate_digit;
            }
            if(continuity !=0)
            {
                duplicate_cnt += duplicate_digit*continuity-Integer.toString(continuity+1).length();
            }
            if(duplicate_cnt!=0)
            {
            int len_ans = s.length()-duplicate_cnt;
            if(answer >len_ans) answer = len_ans;
            }
        }
        return answer;
    }
}