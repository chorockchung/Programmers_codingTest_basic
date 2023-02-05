import math

def solution(n):
    for i in range(max(n, 6), (n * 6 + 1)):
        if (i % n == 0 and i % 6 == 0):
            break      
    return i / 6