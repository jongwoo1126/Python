# 카운트
def Counter(n):
    if n == 0:
        return 0
    else:
        Counter(n-1)

print('n=0 : ', Counter(0))

Counter(5)

# 1 ~ n 정수 누적합
def Adder(n):
    if n == 1:
        return  1
    else:
        result = n +Adder(n-1)

        print(n, end = ' ')
        return result

print('n=1 :', Adder(1))

print('\nn=5 :', Adder(5))

