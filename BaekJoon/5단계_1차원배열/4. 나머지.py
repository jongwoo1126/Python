n = []

for _ in range(10):
    a = int(input())
    b = a % 42
    n.append(b)

n2 =set(n)

print(len(n2))
