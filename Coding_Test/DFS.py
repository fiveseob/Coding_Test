# def DFS(graph, num, visited):
#     visited[num] = True
#     print(num, end=' ')
#     for i in graph[num]:
#         if not visited[i]:
#             DFS(graph,i,visited)
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
# DFS(graph,1,visited)



# # graph를 입력으로 받는 방법도 있음.
# def DFS(graph, num, visited):
#     visited[num] = True
#     print(num, end=' ')
#     for i in graph[num]:
#         if not visited[i]:
#             DFS(graph,i,visited)
#
# n = int(input())
# graph = []
# for i in range(n):
#     graph.append(list(map(int,input().split())))
#
# print(graph)
# visited = [False]*9
# DFS(graph,1,visited)

## practice 1

def DFS(graph, node, visited):
    visited[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if not visited[i]:
            DFS(graph, i, visited)

n = int(input())
graph = []
visited = [False]*9
for i in range(n):
    graph.append(list(map(int,input().split())))

DFS(graph, 1, visited)
