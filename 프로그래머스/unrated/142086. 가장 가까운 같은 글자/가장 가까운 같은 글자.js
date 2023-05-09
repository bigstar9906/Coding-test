function solution(s) {
    var answer = [];
    let map = new Map();
    for(step=0;step<s.length;step++){
        var c = s.charAt(step);
        if(map.has(c)){
           answer.push(step-map.get(c));
        }else{
            answer.push(-1);
        }
        map.set(c,step);
    }
    return answer;
}