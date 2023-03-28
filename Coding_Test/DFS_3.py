# def DFS(graph,visited,start):
#     visited[start] = True
#     print(start, end=' ')
#
#     for i in graph[start]:
#         if not visited[i]:
#             DFS(graph,visited,i)
#     # return 0

def DFS(graph, visited, start):
    visited[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            DFS(graph, visited, i)
graph = [[0],
         [2, 3, 8],
         [1, 7],
         [4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]]

visited = [False]*len(graph)


DFS(graph,visited,1)