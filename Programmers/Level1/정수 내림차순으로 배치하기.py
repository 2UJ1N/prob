#
# [level 1] 정수 내림차순으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12933

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(n):
    num = list(str(n))
    num.sort(reverse = True)
    return int(''.join(num))