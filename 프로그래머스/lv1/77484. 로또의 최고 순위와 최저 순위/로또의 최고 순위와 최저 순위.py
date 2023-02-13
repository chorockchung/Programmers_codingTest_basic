def solution(lottos, win_nums):
    answer = []
    
    num_cnt, zero_cnt = 0, 0
    for num in lottos:
        if(num in win_nums):
            num_cnt += 1
        if(num == 0):
            zero_cnt += 1
            
    return [7 - num_cnt - zero_cnt if num_cnt + zero_cnt != 0 else 6, 7 - num_cnt if num_cnt >= 2 else 6]