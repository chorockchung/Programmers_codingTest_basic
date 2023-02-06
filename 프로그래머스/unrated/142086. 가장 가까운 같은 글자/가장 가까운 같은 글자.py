def solution(s):
    answer = [-1]

    for i in range(1, len(s)):
        cnt = 1
        flag = 0 
        for j in s[i - 1::-1]: 
            if(s[i] == j):
                flag = 1
                break
            cnt += 1
        if(flag):
            answer.append(cnt)
        else:
            answer.append(-1)   
         
    return answer