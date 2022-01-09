"""
날짜 : 2022/01/09
이름 : 박종우
내용 : 최댓값/최솟값 알고리즘 실습 교제 p104
"""

import random
dateset = []
for i in range(10):
    r = random.randint(1, 100)
    dateset.append(r)

print(dateset)

vmax = vmin = dateset[0]

for i in dateset:
    if vmax < i:
        vmax = i
    if vmin > i:
        vmin = i

print('max = ', vmax, 'min = ', vmin)