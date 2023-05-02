#1. 짝지어 제거하기
## 내 코드 : 효율성 실패,,,

def solution(s):
    while len(s) > 1:
        old_s = s
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                s = s.replace(s[i:i + 1], '')
                break
        if old_s == s:
            break

    if len(s) == 0:
        answer = 1
    else:
        answer = 0

    return answer

## 예시 답안
def solution(s):
    answer = 0
    s = list(s)
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    if len(stack) == 0:
        answer = 1

    return answer


## 오늘은 바빴다,,,
