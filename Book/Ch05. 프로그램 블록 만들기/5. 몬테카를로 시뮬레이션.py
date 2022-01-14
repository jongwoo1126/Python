"""
날짜 : 2022/01/09
이름 : 박종우
내용 : 파이썬 몬테카를로 시뮬레이션 실습 p127
"""
import random

def coin(n):
    result = []
    for i in range(n):
        r = random.randint(0, 1)
        if (r == 1):
            result.append(1)
        else:
            result.append(0)

    return result

print(coin(10))


def montacoin(n) :
    cnt = 0
    for i in range(n):
        cnt += coin(1)[0]

    result = cnt / n
    return result

print(montacoin(10))
print(montacoin(30))
print(montacoin(100))
print(montacoin(1000))
print(montacoin(10000))