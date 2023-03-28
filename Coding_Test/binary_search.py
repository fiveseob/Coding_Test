def binary_search(array, target, start, end):
    if start > end:
        return "Don't detect"

    mid = (start + end) // 2
    if array[mid] == target:
        return mid + 1

    if array[mid] > target:
            return binary_search(array, target, start, mid - 1)
    else:
            return binary_search(array, target, mid + 1, end)

N, target = map(int,input().split())
array = list(map(int,input().split()))

print(binary_search(array,target,0,N-1))

# def binary_search(array, target, start, end):
#     while start <= end:
#
#         mid = (start + end) // 2
#         if array[mid] == target:
#             return mid + 1
#
#         if array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     return "dont detect"
#

# from bisect import bisect_left, bisect_right
# def count_by_bisect(array, left, right):
#     left_idx = bisect_left(a, left)
#     right_idx = bisect_right(a, right)
#
#     return right_idx - left_idx
#
# a = [1,2,3,3,3,3,4,4,8,9]
# # 값이 4인 요소의 개수
# print(count_by_bisect(a,4,4))
# # -1에서 3사이에 있는 값의 개수
# print(count_by_bisect(a,-1,3))
#
# print(count_by_bisect(a,1,2))

from bisect import bisect_right, bisect_left

def count(array, search):
    left_idx = bisect_left(array,search)
    right_idx = bisect_right(array,search)

    return right_idx - left_idx

data = [1,1,2,2,2,2,3]
x = 2
print(count(data,x))
