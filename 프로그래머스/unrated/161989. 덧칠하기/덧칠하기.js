function solution(n, m, section) {
    var answer = 0;
    var endPoint =0;
    for(step=0;step<section.length;step++){
        if(section[step]>endPoint){
            answer+=1;
            endPoint=section[step]+m-1;
        }
    }
    return answer;
}