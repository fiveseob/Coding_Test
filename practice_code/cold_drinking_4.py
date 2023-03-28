from collections import deque
def BFS(x, y):
    if graph[x][y] == 0:
        print("x, y : {} {}".format(x, y))
        graph[x][y] = 1
        queue.append([x, y])

        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or ny < 0 or nx >= N or ny >= M:
                    continue
                if graph[nx][ny] == 1:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append([nx, ny])
        return True

N, M = map(int, input().split())

graph = []
count = 0

for i in range(N):
    graph.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

for i in range(N):
    for j in range(M):
        if BFS(i, j) == True:
            count += 1

print(count)
print(graph)

# 3 3
# 001
# 010
# 101
#
# 4 4
# 0011
# 1101
# 0010
# 0010