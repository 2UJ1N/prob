#
# [level 0] 문자열 정렬하기 (1)
# https://school.programmers.co.kr/learn/courses/30/lessons/120850

# 결과
# 정확성: 100.0
# 합계: 100.0 / 100.0

def solution(my_string):
    answer = [int(i) for i in my_string if i.isdigit()]
    answer.sort()

    return answer