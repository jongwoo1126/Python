m = int(input())
n = int(input())
list = []

for i in range(m, n+1):
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                list.append(i)
            break
if len(list) == 0:
    print(-1)
else:
    print(sum(list))
    print(list[0])