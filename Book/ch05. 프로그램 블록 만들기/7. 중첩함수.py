"""
날짜 : 2022/01/09
이름 : 박종우
내용 : 파이썬 중첩함수 실습
"""

# 일급함수와 클로저 p134
def a():
    print('a 함수')
    def b():
        print('b 함수')
    return b
b = a()
b()

data = list(range(1, 101))
def outer_func(data):
    dataSet = data
    def tot():
        tot_val = sum(dataSet)
        return tot_val
    def avg(tot_val):
        avg_val = tot_val / len(dataSet)
        return avg_val
    return tot, avg

tot, avg = outer_func(data)

tot_val = tot()
print('tot =', tot_val)
avg_val = avg(tot_val)
print('avg = ', avg_val)

# 산포도
from statistics import mean
from math import sqrt

data = [4, 5, 3.5, 2.5, 6.3, 5.5]

def scattering_func(data):
    dataSet = data

    def avg_func():
        avg_val = mean(dataSet)
        return avg_val
    def var_func(avg):
        diff = [(data - avg)**2 for data in dataSet]
        print(sum(diff))
        var_val = sum(diff) / (len(dataSet) - 1)
        return var_val
    def std_func(var):
        std_val = sqrt(var)
        return std_val

    return avg_func, var_func, std_func

print('평균 : ', avg())
print('분산 : ', var(avg()))
print('표준편차 : ', std(var(avg())))