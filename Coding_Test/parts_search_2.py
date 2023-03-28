import sys
input = sys.stdin.readline
N = int(input())
datas = list(map(int,input().split()))

M = int(input())
needs = list(map(int,input().split()))

datas.sort()

def binary_search(datas,target,start,end):
    while start <= end:
        mid = (start + end) // 2

        if target == datas[mid]:
            return True
        elif target < datas[mid]:
            end = mid - 1
        else:
            start = mid + 1


for need in needs:
    if binary_search(datas,need,0,N-1) == True:
        print("yes", end=' ')
    else:
        print("no", end=' ')


# 5
# 8 3 7 9 2
# 3
# 5 7 9