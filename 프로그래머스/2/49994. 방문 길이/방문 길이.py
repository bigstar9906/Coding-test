def solution(dirs):
    answer = 0
    row_game_map=[]
    col_game_map=[]
    one_row = [0,0,0,0,0,0,0,0,0,0]
    for i in range(11):
        row_game_map.append(one_row[:])
    one_row.append(0)
    for i in range(10):
        col_game_map.append(one_row[:])
    start_loc = [5,5]
    for directory in dirs:
        if directory =='U' or directory=="D":
            if directory=='U':
                if start_loc[0]>0:
                    start_loc[0]-=1
                    if col_game_map[start_loc[0]][start_loc[1]]==0:
                        answer+=1
                        col_game_map[start_loc[0]][start_loc[1]]=1
            else :
                if start_loc[0]<10:
                    start_loc[0]+=1 
                    if col_game_map[start_loc[0]-1][start_loc[1]]==0:
                        answer+=1
                        col_game_map[start_loc[0]-1][start_loc[1]]=1
        else :
            if directory=='L':
                if start_loc[1]>0:
                    start_loc[1]-=1 
                    if row_game_map[start_loc[0]][start_loc[1]]==0:
                        answer+=1
                        row_game_map[start_loc[0]][start_loc[1]]=1
            else :
                if start_loc[1]<10:
                    start_loc[1]+=1 
                    if row_game_map[start_loc[0]][start_loc[1]-1]==0:
                        answer+=1
                        row_game_map[start_loc[0]][start_loc[1]-1]=1    
    return answer