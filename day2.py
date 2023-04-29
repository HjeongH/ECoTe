# ch4. 구현 #

#1. 상하좌우 ---------------------------------------------
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

#2. 시각
