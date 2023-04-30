'''
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
'''

# 3. 숫자 문자열과 영단어
## 내 코드
## 예시 답안


# 4. 실패율
## 내 코드
## 예시 답안


# 5. 다트 게임
## 내 코드
## 예시 답안


# 6. 로또의 최고 순위와 최저 순위
## 내 코드
## 예시 답안


# 7.  크레인 인형 뽑기 게임
## 내 코드
## 예시 답안


# 8. 키패드 누르기
## 내 코드
## 예시 답안


# 9. 성격 유형 검사하기
## 내 코드
## 예시 답안


# 10. 개인정보 수집 유효기간
## 내 코드
## 예시 답안