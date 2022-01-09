"""
날짜 : 2022/01/09
이름 : 박종우
내용 : 파이썬 내장함수 실습 p116
"""

# builtins
help(len)
dataset = list(range(1, 6))
print(dataset)

print('len = ', len(dataset))
print('sum = ', sum(dataset))
print('max = ', max(dataset))
print('min = ', min(dataset))

# import
import statistics
from statistics import variance, stdev

print('평균 = ', statistics.mean(dataset))
print('중위수 = ', statistics.median(dataset))
print('표본분산 = ', variance(dataset))
print('표본 표준편차 = ', stdev(dataset))