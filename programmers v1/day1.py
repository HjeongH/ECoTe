#1. 짝수와 홀수
## 내 코드
def solution(num):
    answer = ''
    if int(num)%2 == 0:
        answer = 'Even'
    else :
        answer = 'Odd'
    return answer

#2. 약수의 합

## 내 코드 : 에러 발생
def solution(n):
    data = []
    answer = 0
    for i in range(1,3001):
        if n%i == 0 :
            data.append(i)
    answer = int(sum(data))
    return answer

## 구글링 코드
def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n % i == 0: answer += i
    return answer

## 모범답안 참고 코드
def solution(n):
    answer = 0
    for i in range(1,n//2+1): #절반까지만 확인해봐도 괜찮다
        if n%i == 0 :
            answer += i + (n//i)
    return answer

#3. 평균구하기
def solution(arr):
    answer = sum(arr) / len(arr)
    return answer

#4. 번호 가리기
## 내 코드
def solution(phone_number):
    answer = ''
    for i in range(len(phone_number)-4):
        answer += '*'
    answer += phone_number[len(phone_number)-4:]
    return answer

## 모범 답안
def hide_numbers(s):
    return "*"*(len(s)-4)+s[-4:]

#5. 음양 더하기
## 내 코드
def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] == True:
            answer += absolutes[i]
        else :
            answer -= absolutes[i]
    return answer

## 모범 답안
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))


#6. 제일 작은 수 제거하기
## 내 코드
def solution(arr):
    if len(arr) == 1:
        answer = [-1]
    else :
        small = min(arr)
        answer = arr
        answer.remove(small)

    return answer

## 모범 답안
def rm_small(mylist):
    # 함수를 완성하세요
    return [i for i in mylist if i > min(mylist)]


#7. 가운데 글자 가져오기
## 내 코드
def solution(s):
    mid_num = len(s) // 2

    if len(s) % 2 == 0:
        answer = s[mid_num - 1:mid_num + 1]
    else:
        answer = s[mid_num]
    return answer

## 모범 답안
def string_middle(str):
    return str[(len(str)-1)//2 : len(str)//2 + 1]


#8. 부족한 금액 계산하기
## 내 코드
def solution(price, money, count):
    total = 0

    for i in range(count):
        total += price * (i + 1)

    if total <= money:
        answer = 0
    else:
        answer = total - money

    return answer


## 모범 답안
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)