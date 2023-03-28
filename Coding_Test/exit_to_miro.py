from collections import deque
N, M = list(map(int,input().split()))

graph = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    graph.append(list(map(int,input())))

def BFS(x, y):
    queue = deque() # 큐 선언하고
    queue.append([x, y])
    while queue: # 큐 빌때까지 반복, 더 이상 갈때가 없을때 까지
        x, y = queue.popleft() # 큐에서 선입선출 수행
        for i in range(4): # 움직일 수 있는 모든 경우의 수
            step_x, step_y = x + dx[i], y + dy[i] # steps의 순서대로 하나씩 움직여 봄
            if step_x < 0 or step_x >= N or step_y < 0 or step_y >= M: # 행렬 벗어나면 아웃
                continue
            if graph[step_x][step_y] == 0: # 움직인 곳이 0이면 아웃
                continue
            if graph[step_x][step_y] == 1: # 움직인 곳이 1이면
                graph[step_x][step_y] = graph[x][y] + 1 # 방금 있던 곳 + 1 을 움직인 곳에 할당 그리고 그 다음 움직임 수행
                queue.append([step_x, step_y]) # 방문한 노드 위치 (행렬 기준) 삽입
    print(graph)
    return graph[N-1][M-1]

print(BFS(0,0))