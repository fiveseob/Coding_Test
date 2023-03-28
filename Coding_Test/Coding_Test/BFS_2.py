from collections import deque

def BFS(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [[],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6 , 8],
         [1, 7]]

start = 1
visited = [False]*9

BFS(graph, start, visited)