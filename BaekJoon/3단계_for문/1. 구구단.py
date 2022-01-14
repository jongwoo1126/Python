N = int(input())

if 1<=N<=9:

    for i in range(1,10):
        A = N * i
        print('{} * {} = {}'.format(N, i, A))