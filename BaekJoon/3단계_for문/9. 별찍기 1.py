N = int(input())

for i in range(1, N+1):
    print('*' * i)

for i in range(1, N+1):
    for j in range(i):
        print('*', j='')
    print()