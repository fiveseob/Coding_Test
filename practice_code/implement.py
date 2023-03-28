# 1. 시각

n = int(input())
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if (str(i)+str(j)+str(k)).count("3"):
                count +=1

print(count)
