def DFS(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        DFS(x - 1, y)
        DFS(x + 1, y)
        DFS(x, y - 1)
        DFS(x, y + 1)
        print("pass")
        return True
    return False

N, M = list(map(int,input().split()))
graph = []
count = 0
for i in range(N):
    graph.append(list(map(int,input())))
print(graph)


for i in range(N):
    for j in range(M):
        if DFS(i,j) == True:
            count += 1

print(count)

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# def DFS(x, y):
#     if x < 0 or x >= N or y < 0 or y >= M:
#         return False
#
#     if graph[x][y] == 0:
#         graph[x][y] = 1
#         for i in range(4):
#             DFS(x + dx[i], y + dy[i])
#         print("pass")
#         return True
#     return False
#
# N, M = list(map(int,input().split()))
# graph = []
# count = 0
# for i in range(N):
#     graph.append(list(map(int,input())))
# print(graph)
#
#
# for i in range(N):
#     for j in range(M):
#         if DFS(i,j) == True:
#             print("pass 2")
#             count += 1
#
# print(count)