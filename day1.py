# ch3. 그리디 #

#1. 거스름돈 ---------------------------------------------
## 직접짜기
money = int(input("입력받은 돈은"))

won500 = money // 500
money = money - won500*500

won100 = money // 100
money = money - won100*100

won50 = money // 50
money = money - won50*50

won10 = money // 10

print(won500, won100, won50, won10)

## 예시
n = 1260
count = 0

cointypes = [500,100,50,10]


for coin in cointypes :
    count += n // coin
    n %= coin

print(count)

#2. 큰수의 법칙 ---------------------------------------------
#모범답안1
n,m,k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True :
    for i in range(k):
        if m == 0 :
            break
        result += first
        m -= 1

    if m == 0 :
        break
    result += second
    m -= 1

print(result)

#모범답안2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = int(m / (k+1)) * k #왜 //이 아니고 /일까?
count += (m % (k+1))

result = 0
result += count * first
result += (m-count) * second

print(count)

#직접 해보기
n, m, k = map(int, input().split())

data = list(map(int, input().split()))
data.sort(reverse= True)
first = data[0]
second = data[1]

n_blocks, n_rest = map(int,(divmod(m,(k+1))))

result = 0
result = (first*k + second) * n_blocks
result += first*n_rest

print(result)

#3. 숫자 카드 게임 ---------------------------------------------
#직접해보기
n, m = map(int, input().split())

result = []
for i in range(n):
    data = list(map(int,input().split()))
    result.append(min(data))


print(max(result))

#모범답안1
n,m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)

    result = max(result,min_value)

print(result)

#모범답안2
n,m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data :
        min_value = min(min_value,a)
    result = max(result, min_value)

print(result)


#4. 1이 될 때까지 ---------------------------------------------
#직접해보기
n, k = map(int, input().split())

count = 0
while n != 1:
    if n%k == 0:
        n = n//k
    else:
        n -= 1
    count += 1

print(count)

#모범답안1
n, k = map(int, input().split())
result = 0

while n >= k : #이걸 왜 나눠서 해야하지?
    while n%k != 0 :
        n -= 1
        result += 1
    n //= k
    result += 1

while n < k:
    n -= 1
    result += 1

print(result)

# 모범답안2
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break

    result += 1
    n //= k

result += (n - 1)

print(result)
