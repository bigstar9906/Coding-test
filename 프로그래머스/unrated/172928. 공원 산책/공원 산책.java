class Solution {
    public int[] solution(String[] park, String[] routes) {
        int[] answer = new int[2];
        int current_X = 0;
        int current_Y = 0;
        boolean valid = true;
        int temp_X=0;
        int temp_Y=0;
        int MAX_X = park[0].length();
        int MAX_Y = park.length;
        for(int i=0;i<park.length;i++){
            if(park[i].contains("S")){
                current_X = park[i].indexOf("S");
                current_Y = i;
            }
        }
        for(int i=0;i<routes.length;i++){
            String[] split = routes[i].split(" ");
            String direct = split[0];
            int cnt = Integer.parseInt(split[1]);
            temp_X = current_X;
            temp_Y = current_Y;
            valid = true;
            for(int c = 0;c<cnt;c++){
                switch(direct){
                    case "N":
                        if(temp_Y-1>-1){
                            if(park[temp_Y-1].charAt(temp_X)!='X'){
                                temp_Y -=1;
                            }
                            else valid = false;
                        }else {
                            valid = false;
                        }
                        break;
                    case "E":
                        if(temp_X+1<MAX_X){
                            if(park[temp_Y].charAt(temp_X+1)!='X'){
                                temp_X +=1;
                            }else valid = false;
                        }else{
                            valid = false;
                        }
                        break;
                    case "W":
                        if(temp_X-1>-1){
                            if(park[temp_Y].charAt(temp_X-1)!='X'){
                                temp_X -=1;
                            }else valid = false;
                        }else valid = false;
                        break;
                    case "S":
                        if(temp_Y+1<MAX_Y){
                            if(park[temp_Y+1].charAt(temp_X)!='X'){
                                temp_Y +=1;
                            }else valid = false;
                        }else{
                            valid = false;
                        }
                        break;
                }
            }
            if(valid){
                current_X =temp_X;
                current_Y = temp_Y;
            }
        }
        answer[0] = current_Y;
        answer[1] = current_X;
        return answer;
    }
}