import java.lang.Math;
class Solution {
    public long solution(int r1, int r2) {
        return pointNum(r2)-pointNum(r1)+pointNum_Edge(r1);
    }
    
    public long pointNum(long r) {
        long result=0;
        for(long i=0;i<=r;i++){
            result+=Math.floor(Math.sqrt(r*r-i*i))+1;
        }
        return (result-(r+1))*4+1;
        }
    
    public long pointNum_Edge(long r){
        long result =0;
        double temp =0;
        for(long i=0;i<r;i++){
            temp = Math.sqrt(r*r-i*i);
            if(temp==Math.floor(temp)){
                result+=1;
            }
        }
        return result*4;
    }
    
}