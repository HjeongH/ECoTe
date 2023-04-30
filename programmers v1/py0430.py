
#1. 3진법 뒤집기
## 내 코드
def solution(n):
    reverse3 = ''
    while n >=3 :
        reverse3 = str(reverse3) + str(n%3)
        n = n//3
    reverse3 = str(reverse3) + str(n)

    answer = 0
    for i in range(len(reverse3)):
        answer += (3**i) * int(reverse3[(len(reverse3)-i-1)])
    return answer

## 예시 답안
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer


# 2. 1차 비밀지도
## 내 코드
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        num1 = int(arr1[i])
        num2 = int(arr2[i])

        answer_list = []

        for j in range(n-1):
            r = num1 % 2 + num2 % 2
            answer_list.append(r)
            num1 = num1//2
            num2 = num2//2

        answer_list.append(num1 + num2)
        answer_list.reverse()

        result = ''
        for k in answer_list :
            if k == 0 : result += str(' ')
            else : result += str('#')

        answer.append(result)
    return answer

## 예시 답안
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer


# 3. 숫자 문자열과 영단어
## 내 코드
def solution(s):
    words_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(len(words_list)):
        s = s.replace(words_list[i], str(num_list[i]))

    return int(s)

## 예시 답안
num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


# 4. 실패율
## 내 코드 :: 런타임 에러
def solution(N, stages):
    rate_dic = {}
    for i in range(N):
        up = 0
        down = 0
        for j in stages:
            if j == (i + 1): up += 1
            if j >= (i + 1): down += 1

        rate_dic[(i + 1)] = int(up) / int(down)

    rate_dic = sorted(rate_dic.items(), key=lambda item: item[1], reverse=True)

    result = []
    for k in (rate_dic):
        result.append(k[0])

    return result

## 예시 답안
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count  # 이런 로직은 생각도 못헀다,,,
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)


# 5. 이진변환 반복하기
## 내 코드
def solution(s):
    cnt = 0
    zeros = 0

    while s != "1" :
        cnt_0 = s.count(str(0))
        zeros += cnt_0
        s_length = len(s) - cnt_0

        #이진변환
        new_s = ''
        while s_length >=2:
            new_s += str(s_length%2)
            s_length = s_length//2
        new_s += str(s_length)
        s = new_s[::-1]
        cnt += 1

    return [cnt,zeros]

## 예시 답안
def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        num = s.count('1')
        b += len(s) - num
        s = bin(num)[2:] #binary 함수를 몰랐다
    return [a, b]

