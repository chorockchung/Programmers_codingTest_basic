def solution(n, lost, reserve):
    get = 0
    
    for i, stu in enumerate(sorted(lost)):
        if(stu in reserve):
            get += 1
            continue
        if(stu - 1 in reserve and stu - 1 not in lost):
            get += 1
            reserve.remove(stu-1)
            continue
        if(stu + 1 in reserve and stu + 1 not in lost):
            get += 1
            reserve.remove(stu+1)  
              
    return n - len(lost) + get