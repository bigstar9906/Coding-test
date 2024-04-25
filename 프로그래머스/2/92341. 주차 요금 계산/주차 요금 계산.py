import math
def solution(fees, records):
    answer = []
    cars = dict()
    for record in records:
        split = record.split(" ")
        if split[2] == "IN":
            if split[1] in cars:
                inTime = cars[split[1]]["IN"].split(":")
                outTime = cars[split[1]]["OUT"].split(":")
                outM = int(outTime[0])*60+int(outTime[1])
                inM = int(inTime[0])*60+int(inTime[1])
                cars[split[1]]["ADD"]+=outM-inM
                del cars[split[1]]["OUT"]
            else:
                cars[split[1]] = dict()
                cars[split[1]]["ADD"] = 0
            cars[split[1]]["IN"] = split[0]
        else:
            cars[split[1]]["OUT"] = split[0]
    cars = sorted(cars.items())
    for car in cars:
        inTime = car[1]["IN"].split(':')
        outTime = ['23','59']
        if "OUT" in car[1]:
            outTime= car[1]["OUT"].split(':')
        inM = int(inTime[0])*60+int(inTime[1])
        outM = int(outTime[0])*60+int(outTime[1])
        addM = car[1]["ADD"]
        
        ext = math.ceil((addM+outM-inM-fees[0])/fees[2])
        if ext>0:
            answer.append(ext*fees[3]+fees[1])
        else:
            answer.append(fees[1])
        
            
    return answer