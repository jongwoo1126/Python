"""
날짜 : 2022/01/09
이름 : 박종우
내용 : 파이썬 분산과 표준편차 실습 p125
"""

from statistics import mean, variance
from math import sqrt

dateset = [2, 4, 5, 6, 1, 8]

# 산술평균
def Avg(data):
    avg = mean(data)
    return avg

print('산술평균 = ', Avg(dateset))

#분산 / 표준편차
def var_sd(data):
    avg = Avg(data)
    diff = [(d-avg)**2 for d in data]

    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)

    return var, sd

v, s = var_sd(dateset)
print('분산 : ', v)
print('표준편차 = ', s)
