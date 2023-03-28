import sys
input = sys.stdin.readline

N, M = map(int,input().split())
A, B, direction = map(int,input().split()) # A, B, Direction

array = []

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    array.append(list(map(int,input().split())))

def turn_left():
    global direction
    direction += 1
    if direction == 4:
        direction = 0

turn_time = 0
count = 1

while True:
    turn_left() # 한번 돌아

    nx = A + dx[direction]
    ny = A + dx[direction]

    if nx >= 0 and nx < N and ny >= 0 and ny < M: # 움직인게 맵 안에 있음
        if array[nx][ny] == 0: # 이동하려는 곳이 0이면 가
            array[nx][ny] = 1
            A = nx
            B = ny
            count += 1
            turn_time = 0
        else: # 이동하려는 곳이 1이면 못 가
            turn_time += 1 # 다시 돌아 다음 방향으로!
        if turn_time == 4:
        #네번 다 돌았으면 뒤로 가
            nx = A - dx[direction]
            ny = B - dx[direction]
            if array[nx][ny] == 0:
                A = nx
                B = ny
                turn_time = 0
            else:
                break

print(count)



# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1