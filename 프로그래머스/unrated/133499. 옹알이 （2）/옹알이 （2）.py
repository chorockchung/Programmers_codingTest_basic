import re
p = re.compile('[0]{2,10}')

def solution(babbling):
    cnt = 0
    
    can = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for c in can:
            if(b.find(c) != -1):
                # if(b[b.find(c)+len(c):b.find(c)+len(c)*2] != c):
                if(re.search(c*2, b)):
                    print(b)
                else:    
                    b = b.replace(c, '0')
                    # print(b)
                    if(b.isdigit()):
                        cnt += 1
                        break
                    # if(p.search(b) != None):
                    #     print(p.findall(b), b)
                    #     break

    return cnt