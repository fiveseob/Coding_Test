# Stack

# data = []
#
# data.append(5)
# data.append(2)
# data.append(3)
# data.append(7)
# print(data)
# data.pop()
# print(data)
# data.append(1)
# data.append(4)
# print(data)
# data.pop()
# print(data)
#
#
# print(data)
# print(data[::-1])


# Queue
# from collections import deque
#
# data = deque()
# data.append(5)
# data.append(2)
# data.append(3)
# data.append(7)
# print(data)
# data.popleft()
# print(data)
# data.append(1)
# data.append(4)
# print(data)
# data.popleft()
# print(data)

# print(list(data))
# data.reverse()
# print(list(data))


def recursive_function(i):
    print("재귀 함수를 {}번 호출했음".format(i))
    # print("재귀 함수를",i,"번 호출했음")

    if i == 100:
        return i
    else:
        return recursive_function(i+1)


i = 1
print(recursive_function(i))

# def factorial_recursive(n):
#     if n <= 1:
#         return 1
#
#     else:
#         return n * factorial_recursive(n-1)
#
# result = 5
# print(factorial_recursive(5))