from collections import deque
def BFS(visited, start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
graph = [[0],
         [2, 3, 8],
         [1, 7],
         [4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]]

visited = [False]*9
start = 1

BFS(visited,start)
# queue = deque()
# queue.append(start)
# visited[start] = True
#
# while queue:
#     node = queue.popleft()
#     print(node, end=' ')
#     for i in graph[node]:
#         if not visited[i]:
#             queue.append(i)
#             visited[i] = True