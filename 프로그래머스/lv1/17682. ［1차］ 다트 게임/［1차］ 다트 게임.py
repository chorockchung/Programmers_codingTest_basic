import re
def solution(d):
    # 점수와 옵션은 딕셔너리로 변환
    bonus = {'S' : 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}
    answer = []

    # (\d+) : 정수 (10이상도 찾아줌)
    # ([SDT]) : 'SDT' 인 문자
    # ([*#]?) : '*#' 문자를 찾는데, ? -> 없으면 '' 반환
    # 정규표현식을 이용하여 튜플로 묶어서 리스트로 변환
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(d) # 입력값이 d = '1S2D*10T' 일때
    print(dart)         # [('1', 'S', ''), ('2', 'D', '*'), ('10', 'T', '')] 으로 리스트가 생성됨
    # 3개의 리스트 완전탐색
    for i in dart:
       # 2 index의 옵션이 [ * ]이고 다트를 던진횟수가 1번이상이면
        if i[2] == '*' and len(answer) > 0:
            # 이전에 얻은 점수에 2배
            answer[-1] *= 2
        # 다트점수 + 보너스점수 + 옵션 연산
        answer.append(int(i[0]) ** bonus[i[1]] * option[i[2]])
    return sum(answer)