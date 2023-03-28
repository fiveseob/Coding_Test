
N = int(input())
datas = []
for i in range(N):
    input_data = input().split()
    datas.append([input_data[0],int(input_data[1])])

# result_1 = dict(datas)
result_1 = tuple(datas)
print(result_1)
# result_2 = sorted(result_1.items(), key=lambda x:x[0])
# result_2 = sorted(result_1, key=lambda x:result_1[x])
result_2 = sorted(result_1, key=lambda x:x[1])
print(result_2)
for j in result_2:
    print(j[1],end=' ')

# result_2 = sorted(result_1.items(),reverse=True)
# print(result_1)
# print(result_2)
# for j in result_2:
#     print(j[1],end=' ')
