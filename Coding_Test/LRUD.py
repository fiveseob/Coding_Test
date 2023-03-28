# n = int(input())
# u, v = 1, 1
# moves = list(map(str, input().split()))
# move_type = ['L','R','U','D']
# du = [-1,1,0,0]
# dv = [0,0,-1,1]
#
# for move in moves:
#     for i in range(len(move_type)):
#         if move == move_type[i]:
#                 u += du[i]
#                 v += dv[i]
#
#         if (v == 0) or (v == n+1):
#             v += 1
#         if (u == 0) or (u == n+1):
#             u += 1
#
# print("{} {}".format(v,u))

n = int(input())

moves = list(map(str,input().split()))

move_type = ['L','R','U','D']
du = [-1, 1, 0, 0]
dv = [0, 0, -1, 1]

u, v = 1, 1

for move in moves:
    for i in range(len(move_type)):
        if move == move_type[i]:
           u += du[i]
           v += dv[i]
    if u < 1 or u > n:
        u += 1
    if v < 1 or v > n:
        v += 1
print(v, u)



