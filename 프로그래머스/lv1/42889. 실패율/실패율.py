def solution(N, stages):
    users = [0]
    failureRate = dict()    
    leftStages = len(stages)

    for i in range(1, N+1):
        users.append(stages.count(i))
    for i in range(1, N+1): 
        if(leftStages == 0):
            failureRate[i] = 0
        else:    
            failureRate[i] = users[i]/leftStages
            leftStages -= users[i]

    answer = sorted(failureRate.items(), key=lambda x:x[1], reverse=True)

    return list(dict(answer).keys())