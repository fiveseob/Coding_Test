from collections import deque
def BFS(i, j):
    queue = deque()
    queue.append([i,j])

    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                queue.append([nx,ny])
                graph[nx][ny] = graph[x][y] + 1

    return print(graph[N-1][M-1])
N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

BFS(0,0)

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111