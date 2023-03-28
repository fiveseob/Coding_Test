def DFS(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            DFS(graph, i, visited)

        # 이 개념을  stack 과 연결...? 왜 stack을 쓴다고 하는건지
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

DFS(graph, start, visited)

