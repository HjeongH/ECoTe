# ch5. DFS/BFS #
## 리뷰 필수!!

#1. 음료수 얼려 먹기 ---------------------------------------------
## 예시 답안

n,m = map(int, input().split())

graph= []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x <= -1 or x>= n or y <= -1 or y>=m :
        return False
    if graph[x][y] == 0:
        graph[x][y]=1

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n) :
    for j in range(m):
        if dfs(i,j) == True :
            result += 1

print(result)


#2. 미로 탈출 ---------------------------------------------
## 예시 답안
n,m = map(int, input().split())

graph= []
for i in range(n):
    graph.append(list(map(int, input())))

result = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque
def dfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<=-1 or nx>=n or ny<=-1 or ny>m :
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny] ==1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))
