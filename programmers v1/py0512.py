#1. 영어 끝말잇기
## 내코드
def solution(n, words):
    word_list = []
    word_list.append(words[0])
    answer= []
    for i in range(1, len(words)) :
        before = words[(i-1)][-1]
        now = words[i][0]

        if before != now or words[i] in word_list:
            answer.append(i % n + 1 )
            answer.append((i // n) +1 )
            break
        else :
            word_list.append(words[i])

    if len(words) == len(word_list) :
        answer.append(0)
        answer.append(0)

    return answer

## 예시 답안 : list[:p]를 생각하지 못했다
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]


#2. 괄호 회전하기
## 내코드 :: 왜 오류지?
def solution(s):
    cnt = 0

    for i in range(len(s)):
        txt = s[i:] + s[:i]

        ck_list = []
        for j in range(0, len(txt)):
            if txt[j] == ')' and '(' not in ck_list:
                break
            elif txt[j] == '}' and '{' not in ck_list:
                break
            elif txt[j] == ']' and '[' not in ck_list:
                break
            else:
                ck_list.append(txt[j])

        if len(ck_list) == len(txt):
            cnt += 1

    return cnt

## 예시 답안
def solution(s):
    ans, pair = 0, {'{':'}', '[':']', '(':')'}
    for i in range(len(s)):
        iscorrect, stack = True, []
        for v in s:
            if v in ['{','[','(']: stack.append(v)
            elif not stack or v != pair[stack[-1]]: iscorrect = False
            else: stack = stack[:-1]

        ans += int(iscorrect and not stack)
        s = s[1:]+s[0]

    return ans

# 3. n^2 배열 자르기
## 내코드

## 예시 답안 : max를 쓸 생각을 못했다
def solution(n, left, right):
    answer = []
    for i in range(left,right+1):
        answer.append(max(i//n,i%n)+1)
    return answer

# 4. k진수에서 소수 개수 구하기
## 내코드 : 소수 확인할 때 시간초과 문제가 발생해서, sqrt를 썼다
import math

def solution(n, k):
    # k진수로 표현하기
    num = ''
    while n > k:
        num = num + str(n % k)
        n = n // k

    num += str(n)
    num = num[::-1]

    answer = list(num.split('0'))

    cnt = 0
    for i in answer:
        ck = 0

        if i == '' or i == '1':
            continue
        else:
            i = int(i)
            for j in range(2, int(math.sqrt(i) + 1)):

                if i % j == 0:
                    ck += 1
                    break
            if ck == 0:
                cnt += 1

    return cnt


# 5.
## 내코드
## 예시 답안

