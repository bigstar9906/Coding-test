import java.util.Arrays;
class Solution {
    
    public int answer=-1;
    
    public void dfs(int k, boolean[] visited, int[][] dungeons, int cnt){
        for(int i=0;i<dungeons.length;i++){
            if(!visited[i] && k>=dungeons[i][0]){
                visited[i]=true;
                dfs(k-dungeons[i][1],visited,dungeons,cnt+1);
                visited[i]=false;
            }
        answer = cnt>answer?cnt:answer;
        }
    }
    public int solution(int k, int[][] dungeons) {
        boolean[] visited = new boolean[dungeons.length];
        dfs(k,visited,dungeons,0);
        return answer;
    }
}