from collections import deque

def BFS(x, y):
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            step_x = x + dx[i]
            step_y = y + dy[i]
            if step_x >= N or step_x < 0 or step_y >= M or step_y < 0:
                continue
            if graph[step_x][step_y] == 0:
                continue
            if graph[step_x][step_y] == 1:
                queue.append([step_x, step_y])
                graph[step_x][step_y] = graph[x][y] + 1
    return graph[N-1][M-1]

N, M = list(map(int,input().split()))

graph = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    graph.append(list(map(int,input())))

print(BFS(0,0))





# def BFS(x, y):
#     queue = deque()
#     queue.append([x, y])
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             step_x, step_y = x + dx[i], y + dy[i]
#             if step_x < 0 or step_x >= N or step_y < 0 or step_y >= M:
#                 continue
#             if graph[step_x][step_y] == 0:
#                 continue
#             if graph[step_x][step_y] == 1:
#                 graph[step_x][step_y] = graph[x][y] + 1
#                 queue.append([step_x, step_y])
#     print(graph)
#     return graph[N-1][M-1]
