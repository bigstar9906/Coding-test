def solution(sizes):
    answer = 0
    width =0
    height = 0
    for size in sizes:
        width = max(width,min(size))
        height = max(height,max(size))
    
    return width*height