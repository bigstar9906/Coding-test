function solution(a, b, n) {
    var answer = 0;
    var left = 0;
    var temp = 0;
    while(Math.floor((n+left)/a)>=1){
        temp = (n+left)%a;
        n=Math.floor((n+left)/a)*b;
        left = temp;
        answer+=n;        
    }
    return answer;
}