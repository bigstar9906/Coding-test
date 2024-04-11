import java.util.*;
class Solution {
    private static List<List<Integer>> graph;
    private static boolean[] visited; // 막대 그래프 체크하고 false면 다른 그래프 확인용
    private static int maxVertex; // 정점 최대 번호
    private static int[] incomingEdges; // 다음으로 가는 개수 2개 -> 그 노드로 들어가는 간선이 2개
    private static int[] isIn;
    private static int cnt;
    public int[] solution(int[][] edges) {
        int[] answer = new int[4];
        initGraph(edges);
        int startVertex = findCreatedVertex(); // 정점 찾기
        int graphNum = graph.get(startVertex).size();
        answer[0] = startVertex;
        removeEdgesFromCreatedVertex(startVertex);        
        answer[2] = countBarGraphs(startVertex);
        answer[3] = countEightGraphs();
        answer[1] = graphNum - (answer[2] + answer[3]);
        return answer;
    }
    private void initGraph(int[][] edges) {
        maxVertex = 0;
        for(int[] edge : edges) {
            maxVertex = Math.max(maxVertex, Math.max(edge[0], edge[1]));
        }
        visited = new boolean[maxVertex+1];
        incomingEdges = new int[maxVertex+1];
        isIn = new int[maxVertex+1];
        graph = new ArrayList<>(maxVertex+1);
        for (int i = 0; i <= maxVertex; i++) {
            graph.add(new LinkedList<>());
        }
        for (int i = 0; i < edges.length; i++) {
            graph.get(edges[i][0]).add(edges[i][1]);
            incomingEdges[edges[i][1]]++;
            for(int j=0;j<2;j++){
                if(isIn[edges[i][j]]!=1){
                    isIn[edges[i][j]] = 1;
                    cnt+=1;
                }
            }
        }
    }
    private static int countEightGraphs() {
        int count = 0;
        for (int i = 1; i < graph.size(); i++) {
            if ( incomingEdges[i] == 2) {
                count++;
            }
        }
        return count;
    }
    private static int countBarGraphs(int startVertex) {
        int count = 0;
        for (int i = 1; i < graph.size(); i++) {
            if (i == startVertex) continue;
            if (incomingEdges[i]== 0) {
                count++;
                visited[i] = true;
            }
        }
        count -= graph.size()-cnt-1;
        return count;
    }
    private static int findCreatedVertex() {
        // int createdVertex = -1;
        for (int i = 1; i < graph.size(); i++) {
            if(graph.get(i).size() >= 2 && incomingEdges[i] == 0) {
                visited[i] = true;
                return i;
            }
        }
        return -1;
    }
    private static void removeEdgesFromCreatedVertex(int vertex) {
        for (int end:graph.get(vertex)) {
            incomingEdges[end]-=1;
        }
        graph.set(vertex, new LinkedList<>());
    }
}