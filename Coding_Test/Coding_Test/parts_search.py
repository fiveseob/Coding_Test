# # 1
# N = int(input())
# datas = list(map(int,input().split()))
#
# M = int(input())
# input_array = list(map(int,input().split()))
# result = [0]*M
# check = False
#
# datas.sort()
#
# for i in range(len(input_array)):
#     for j in range(len(datas)):
#         if datas[j] == input_array[i]:
#             check = True
#         else:
#             pass
#     if check == True:
#         result[i] = 1
#         check = False
#     else:
#         pass
#
# for k in result:
#     if k == True:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')

# # 2 for문 줄이기. pythonic 하게 짜기 ㅎ
# N = int(input())
# datas = list(map(int,input().split()))
#
# M = int(input())
# input_array = list(map(int,input().split()))
#
# print(len(input_array))
# for i in range(len(input_array)):
#     if input_array[i] in datas:
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')

# 3 재귀함수(이진탐색) 써보기
def binary_search(datas,target,start,end):
    if start > end:
        return None
    mid = (start + end) // 2
    if datas[mid] == target:
        return True
    if datas[mid] > target:
        return binary_search(datas,target,start,mid - 1)
    else:
        return binary_search(datas,target,mid + 1, end)

N = int(input())
datas = list(map(int,input().split()))

M = int(input())
input_array = list(map(int,input().split()))

datas.sort()

for i in range(len(input_array)):
    if binary_search(datas,input_array[i],0,N-1):
        print("yes", end=' ')
    else:
        print("no", end=' ')

# def binary_search(datas,target,start,end):
#     while start <= end:
#         if start > end:
#             return None
#         mid = (start + end) // 2
#         if datas[mid] == target:
#             return True
#         if datas[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#
# N = int(input())
# datas = list(map(int,input().split()))
#
# M = int(input())
# input_array = list(map(int,input().split()))
# datas.sort()
# for i in range(len(input_array)):
#     if binary_search(datas,input_array[i],0,N-1):
#         print("yes", end=' ')
#     else:
#         print("no", end=' ')
