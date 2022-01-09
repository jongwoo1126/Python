"""
날짜 : 2022/01/09
이름 : 박종우
내용 : 파이썬 특수함수 실습 p129
"""

# 튜플형 가변인수
def Func1(name, *names):
    print(name)
    print(names)

Func1('홍길동', '이순신', '유관순')

# 통계량 구하는 함수
from statistics import mean, variance, stdev     #statistics 모듈 import

def statis(func, *data):
    if func == 'avg':
        return mean(data)
    elif func == 'var':
        return variance(data)
    elif func == 'std':
        return stdev(data)
    else:
        return 'TypeError'

print('avg =', statis('avg', 1, 2, 3, 4, 5))
print('var =', statis('var', 1, 2, 3, 4, 5))
print('std =', statis('std', 1, 2, 3, 4, 5))

# 딕트형 가변인수
def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)

emp_func('홍길동', 35, addr = '서울시', height = 175, weight = 65)

# 람다함수
def Adder(x, y):
    add = x + y
    return  add
print('add = ', Adder(10, 20))

print('add =', (lambda x, y : x + y)(10, 20))

# 함수 스코프
x = 50
def local_func(x):
    x += 50
local_func(x)
print('x = ', x)

def global_func():
    global x
    x += 50
global_func()
print('x = ', x)