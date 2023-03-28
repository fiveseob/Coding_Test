start = input()
x, y = ord(start[0]) - ord('a'), int(start[1]) - 1

dx = [-2, -2, -1, 1, 2, 2, 1, -1]
dy = [-1, 1, 1, 2, 1, -1, -2, -2]
count = 0
miss = 0
for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or ny < 0 or nx >= 8 or ny >= 8:
        continue
    else:
        count += 1

print(count)