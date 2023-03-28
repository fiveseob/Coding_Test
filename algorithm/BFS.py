# from collections import deque
#
# def BFS(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#
#     while queue:
#         node = queue.popleft()
#         print(node, end=' ')
#         for i in graph[node]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
# graph = [[],
#          [2,3,8],
#          [1,7],
#          [1,4,5],
#          [3,5],
#          [3,4],
#          [7],
#          [2,6,8],
#          [7]]
# visited = [False]*9
# BFS(graph,1,visited)

from collections import deque
def BFS(graph, node, visited):
    queue = deque([node])
    visited[node] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

visited = [False]*9
BFS(graph,1,visited)