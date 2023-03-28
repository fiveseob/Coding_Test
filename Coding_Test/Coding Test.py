# n, m, k = map(int, input().split())
#
# data = list(map(int, input().split()))
#
# data.sort()
# max_fst = data[n-1]
# max_snd = data[n-2]
#
# result = 0
#
# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += max_fst
#         m -= 1
#
#     if m == 0:
#         break
#     result += max_snd
#     m -= 1
#
# print(result)

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
max_fst = data[n-1]
max_snd = data[n-2]

result = (max_fst * k + max_snd) * ( m // (k+1))
result += max_fst * ( m % (k+1))

print(result)