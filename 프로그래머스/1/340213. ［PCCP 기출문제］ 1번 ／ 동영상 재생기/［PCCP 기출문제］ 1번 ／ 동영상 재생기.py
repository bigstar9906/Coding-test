def posToSec(pos):
    posSplit =  pos.split(":")
    return int(posSplit[0])*60+int(posSplit[1])
def secToPos(sec):
    return ""+str(sec//60).zfill(2)+":"+str(sec%60).zfill(2)
def solution(video_len, pos, op_start, op_end, commands):
    if posToSec(op_start)<=posToSec(pos)<=posToSec(op_end):
        pos = op_end
    sec = posToSec(pos)
    endSec = posToSec(video_len)
    for command in commands:
        if command == "prev":
            if sec>10:
                sec-=10
            else:
                sec=0
        else:
            if endSec>sec+10:
                sec+=10
            else:
                sec=endSec
        if posToSec(op_start)<=sec<=posToSec(op_end):
            sec = posToSec(op_end)
    return secToPos(sec)
    