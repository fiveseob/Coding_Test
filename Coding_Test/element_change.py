# # 1
# N, K = map(int, input().split())
# array_A = list(map(int, input().split()))
# array_B = list(map(int, input().split()))
#
# result = []
#
# array_A.sort(reverse=True)
# array_B.sort(reverse=True)
#
# result = array_A[:len(array_A)-K] + array_B[:K]
#
# print(sum(result))
#

# 2
N, K = map(int, input().split())
array_A = list(map(int, input().split()))
array_B = list(map(int, input().split()))

result = []

array_A.sort()
array_B.sort(reverse=True)

for i in range(K):
    if array_A[i] < array_B[i]:
        array_A[i], array_B[i] = array_B[i], array_A[i]
    else: # 예외처리. 연산을 낭비하지 않고 바로 나올 수 있게끔. ㅎㅎ
        break

print(sum(array_A))