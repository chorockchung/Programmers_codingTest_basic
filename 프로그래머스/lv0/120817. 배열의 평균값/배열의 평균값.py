def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i

    return float(answer / len(numbers))