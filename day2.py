# ch4. 구현 #

#1-1. 상하좌우 ---------------------------------------------
## 직접짜기
n = int(input())
x, y =1, 1
plan = list(input().split())

for i in range(len(plan)):
    if (plan[i] == "R") and (y != n) :
       y += 1
    elif (plan[i] == "L") and (y != 1) :
       y -= 1
    elif (plan[i] == "D") and (x != n):
       x += 1
    elif (plan[i] == "U") and (x != 1) :
       x -= 1
print(x, y)

## 예시 답안
n = int(input())
x, y =1, 1
plans = input().split()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny <1 or nx>n or ny>n :
        continue
    x,y = nx,ny

print(x, y)

#1-2. 시각
## 예시 답안 (완전탐색)
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

#2 왕실의 나이트
## 내 코드 (예시 답안 참고)

xy = input()
x= int(ord(xy[0])) - int(ord('a')) + 1
y = int(xy[1])

steps = [(-2,1),(-2,-1),(2,1),(2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]

count = 0
for ck in steps:
    xd = x + int(ck[0])
    yd = y + int(ck[1])

    if xd<1 or yd<1 or xd>8 or yd >8:
        continue
    count += 1

print(count)


#3 게임 개발
## 예시 답안
n, m = map(int,input().split())
x,y,direction = map(int,input().split())
steps = [(-1,0),(0,1),(1,0),(0,-1)] #나눠서 저장하는 방법도 가능

### 방문한 위치 저장 : 혼자서 생각하지 못한 부분
d = [[0] * m for _ in range(n)] #익숙하지 않은 리스트 컴프리헨션 문법
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

count = 1
turn_time = 0 #생각 못한 부분

while True:
    direction -= 1 #사용자 정의 함수로 만들 수도
    if direction == -1 : direction = 3

    nx = x + int(steps[direction][0])
    ny = y + int(steps[direction][1])

    if d[nx][ny]==0 and array[nx][ny]==0 :
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    else :
        turn_time += 1
    if turn_time == 4:
        nx = n - int(steps[direction][0])
        ny = y - int(steps[direction][1])

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else :
            break

    turn_time = 0
print(count)