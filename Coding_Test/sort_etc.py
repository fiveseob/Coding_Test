# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# # array.sort()
# # print(array)
#
# a = sorted(array)
# print(array)
# print(a)

## Q1
# N = int(input())
# datas = []
# for i in range(N):
#     datas.append(int(input()))
#
# # datas.sort(reverse=True)
# result = sorted(datas, reverse=True)
# for j in result:
#     print(j, end=' ')


## Q2
# N = int(input())
# input_data = []
# datas = []
#
# for data in range(N):
#     input_data = input().split()
#     datas.append((input_data[0],int(input_data[1])))
#
# tmp = dict(datas)
# # key에 접근하는 것임, key를 오름차순, 내림차순으로 정렬 가능
# # results = sorted(tmp)
# results = sorted(tmp.items()) #튜플로 바꿈
#
# for result in results:
#     print(result, end=' ')
#
# print("\n",type(tmp))
# print(results)
# print(dict(results))

# # value에 접근하는 방법
#
dic = {'김형래':22,'오장섭':11,'김가나':15}

result = sorted(dic,key=lambda x:dic[x],reverse=True)
print(result)
