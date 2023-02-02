import collections

def solution(array):
    cntr = collections.Counter(array)
    mostArr = cntr.most_common()
    
    cnt = 0
    for i in range(len(mostArr)):
        if(mostArr[0][1] == mostArr[i][1]):
            cnt += 1
    
    if(cnt > 1):
        return  -1
    return mostArr[0][0]