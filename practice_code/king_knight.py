data = input()

x = int(data[1])
y = ord(data[0]) - ord('a') + 1

steps = [[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1]]

count = 0
for step in steps:
    dx = x + step[0]
    dy = y + step[1]

    if dx > 8 or dx < 1:
        continue
    if dy > 8 or dy < 1:
        continue

    count += 1

print(count)
