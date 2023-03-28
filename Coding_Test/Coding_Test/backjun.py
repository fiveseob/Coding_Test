import sys
input = sys.stdin.readline
N, K = map(int,input().split())

datas = list(map(int,input().split()))

result = [0]*(N+1)

for x in range(N):
    result[x+1] = result[x] + datas[x]

for x in range(K):
    start, end = map(int, input().split())
    print(result[end] - result[start - 1])

#
# import sys
# input=sys.stdin.readline
# N,M=map(int,input().split())
# L=list(map(int,input().split()))
# S=[0]*(N+1)
# for i in range(len(L)):
#     S[i+1]=S[i]+L[i]
#
# print(S)
#
# for _ in range(M):
#     i,j=map(int,input().split())
#     print(S[j]-S[i-1])