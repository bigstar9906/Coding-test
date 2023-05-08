function solution(wallpaper) {
    var lux,luy,rdx,rdy;
    for(step =0;step<wallpaper.length;step++){
        var start = wallpaper[step].indexOf('#');
        var end = wallpaper[step].lastIndexOf('#');
        if(wallpaper[step].includes('#')&&lux==null){
            lux = step;
            luy = start;
            rdx = step;
            rdy = end;
        }
        if(start!=-1&&step>rdx) rdx = step;
        if(start!=-1&&start<luy) luy = start;
        if(end>rdy) rdy = end;
    }
    return [lux,luy,rdx+1,rdy+1];
}