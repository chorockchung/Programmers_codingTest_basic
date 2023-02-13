def solution(k, score):
    hall = [0]
    answer = []
    
    m = 0
    for s in score:
        for i, a in enumerate(hall):
            if(s >= a):
                hall.insert(i, s)
                break
        if(m == k):
            answer.append(hall[k-1])
        else:
            answer.append(hall[m])
            m += 1
    return answer