class Solution {
    public int[] solution(int brown, int yellow) {
    for(int i =3;i<2500;i++)
    {
        if(((brown+4)/2 -i)*i==brown+yellow) return new int[]{(brown+4)/2 -i,i};
    }
    
        return new int[]{};
    }
}