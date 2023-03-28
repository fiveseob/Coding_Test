import sys
input = sys.stdin.readline

N, M = map(int,input().split())
datas = list(map(int,input().split()))

datas.sort()

start = 0
end = max(datas)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for data in datas:
        if data > mid:
            total += (data - mid)

    if total < M: # 덜 자른거니 더 자르기 위해 end를 낮춤
        end = mid - 1
    else: # 많이 자른거니 덜 자르기 위해 start를 높임?
        result = mid
        start = mid + 1

print(result)

# 4 6
# 19 15 10 17