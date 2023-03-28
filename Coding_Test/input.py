test = input()
test1 = input().split() # 공백 기준 나눔, str로 나옴
test2 = input().split('.') # . 기준 나눔
test3 = list(map(int,input().split())) # int인 list로 나옴
print(type(test))
print(len(test))
print(test)
print(type(test1))
print(test1)
print(test2)
print(test3)

for i in range(len(test)):
    print(test[i])