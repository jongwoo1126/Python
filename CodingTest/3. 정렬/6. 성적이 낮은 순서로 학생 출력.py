n = int(input())

list = []
a = 0
b = 0
i = a, b
for i in range(n):
    i = input().split()
    list.append(i)

result = sorted(list, key=lambda data:data[1], reverse=True)
print(result)

