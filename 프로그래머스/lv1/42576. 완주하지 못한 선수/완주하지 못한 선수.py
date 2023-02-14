def solution(participant, completion):
    
    participant = sorted(participant)
    completion = sorted(completion)
    
    for i, p in enumerate(participant):
        if(i < len(completion)):
            if(p != completion[i]):
                return p
            
    return p         