# datas = list(input())
#
# alpha = ''
# num = 0
# datas = sorted(datas)
# for data in datas:
#     if data.isalpha():
#         alpha += data
#     else:
#         num += int(data)
# print(alpha+str(num))

datas = list(input())

alpha = []
num = 0
datas = sorted(datas)
for data in datas:
    if data.isalpha():
        alpha.append(data)
    else:
        num += int(data)
alpha.append(str(num))
print(alpha)
print(''.join(alpha))

arr = ['a','b','c']
print(''.join(arr))