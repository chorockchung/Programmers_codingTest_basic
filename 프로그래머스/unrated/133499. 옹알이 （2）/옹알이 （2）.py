import re
p = re.compile('[0]{2,10}')

def solution(babbling):
    cnt = 0
    
    can = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for c in can:
            if(b.find(c) != -1):
                if(re.search(c*2, b) == None):  
                    b = b.replace(c, '0')
                if(b.isdigit()):
                    cnt += 1
                    break

    return cnt