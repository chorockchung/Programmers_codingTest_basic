def solution(k, m, score):
    answer = 0
    #score를 정렬, 최대이익을 내기 위해 뒤부터 계산(앞의 적은 숫자는 버리기 위하여)
    score = sorted(score, reverse=True)
    
    index = m - 1
    while(index < len(score)):
        answer += score[index] * m
        index += m
    return answer