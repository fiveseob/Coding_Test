
N, M = map(int,input().split())
datas = list(map(int,input().split()))

start = 0
end = max(datas)
total = 0

while start <= end:
    mid = (start + end) // 2

    for data in datas:
        if data > mid:
            total += data - mid

    if total >= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
    total = 0
print(result)

# 4 6
# 19 15 10 17