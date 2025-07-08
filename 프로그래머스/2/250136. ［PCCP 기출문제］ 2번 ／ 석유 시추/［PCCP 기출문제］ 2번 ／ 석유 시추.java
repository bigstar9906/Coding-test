import java.util.Queue;
import java.util.LinkedList;
import java.util.Arrays;
import java.util.Vector;
class Solution {
    public int solution(int[][] land) {
        int answer = 0;
        int maxVal = 0;
        Vector<Integer> list = new Vector<>();
        for(int i=0;i<land[0].length;i++){
            list.add(0);
        }
        for(int i=0;i<land.length;i++){
            for(int j=0;j<land[0].length;j++){
                if(land[i][j]==1){
                    int value = 0;
                    int minY = j;
                    int maxY = j;
                    Queue<int[]> q = new LinkedList();
                    q.offer(new int[]{i,j});
                    land[i][j]=0;
                    while(!q.isEmpty()){
                        int[] current = q.poll();
                        int x = current[0];
                        int y = current[1];
                        value+=1;
                        if(x>0 && land[x-1][y]==1){
                            q.offer(new int[]{x-1,y});
                            land[x-1][y]=0;
                        }
                        if(x<land.length-1 && land[x+1][y]==1){
                            q.offer(new int[]{x+1,y});
                            land[x+1][y]=0;
                        }
                        if(y>0 && land[x][y-1]==1){
                            q.offer(new int[]{x,y-1});
                            land[x][y-1]=0;
                            if(minY>y-1){
                                minY=y-1;
                            }
                        }
                        if(y<land[0].length-1 && land[x][y+1]==1){
                            q.offer(new int[]{x,y+1});
                            land[x][y+1]=0;
                            if(maxY<y+1){
                                maxY=y+1;
                            }
                        }                        
                    }
                    for(int k=minY;k<=maxY;k++){
                        int val = list.get(k)+value;
                        list.set(k,val);
                        if(maxVal<val){
                            maxVal=val;
                            answer = maxVal;
                        }
                    }
                }
            }
        }
        return answer;
    }
}