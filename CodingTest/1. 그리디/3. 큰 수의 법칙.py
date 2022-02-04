n, m, k = map(int,input().split())
data = list(map(int, input().split()))

result = 0

data.sort(reverse=True)

first = data[0]
second = data[1]

repeat = k

for i in range(m):

    if repeat > 0:
        result += first
        repeat -= 1
    else:
        result += second
        repeat = k

print(result)

