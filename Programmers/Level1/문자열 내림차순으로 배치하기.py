#
# [level 1] 문자열 내림차순으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12917

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(s):
    n = list(s)
    n.sort(reverse = True)
    return ''.join(n)
