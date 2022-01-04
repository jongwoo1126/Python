"""
날짜 : 2022/01/03
이름 : 박종우
내용 : 파이썬 반복문 for 실습하기 교재 p70
"""

# for
for i in range(5):
    print('반복 i :', i)

for j in range(10, 20):
    print('반복 j :', j)

for k in range(10, 0, -1):
    print('반복 k :', k)

for l in range(10, 0, -3):
    print('반복 k :', l)

# 1부터 10까지 합
tot = 0

for i in range(1, 11):
    tot += i

print('1부터 10까지 합', tot)

# 1부터 10까지 짝수합
sum = 0

for k in range(1, 11):
    if k%2 == 0:
        sum += k

print('1부터 10까지 짝수합', sum)

# 중첩 for
for a in range(3):
    print('a :', a)
    for b in range(4):
        print('b :', b)
        for c in range(5):
            print('c :', c)

# 구구단
for x in range(2,10):
    for y in range(1,10):
        z = x * y
        print('{} x {} = {}'.format(x, y, z))

# 별삼각형
for start in range(1, 11):

    for end in range(start):
        print('A', end='')

    print()  # 줄바꿈

for start in range(1, 11):

    for end in range(11-start):
        print('A', end='')

    print()  # 줄바꿈


for i in range(11):
    print('ㅁ' * i)