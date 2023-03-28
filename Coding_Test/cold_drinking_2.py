def DFS(x, y):
    if x >= N or x < 0 or y >= M or y < 0:
        return False
    if graph[x][y]:
        return False
    if not graph[x][y]:
        graph[x][y] = True
        for i in range(4):
            DFS(x + dx[i], y + dy[i])
        return True

N, M = list(map(int,input().split()))

graph = []
count = 0
for i in range(N):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0] # 상, 하, 좌, 우
dy = [0, 0, -1, 1]
for i in range(N):
    for j in range(M):
        if DFS(i, j):
            count += 1

print(count)
