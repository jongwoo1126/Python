"""
날짜 : 2022/01/04
이름 : 박종우
내용 : 반복문
"""

# while 반복문
cnt = tot = 0
while cnt < 5:
    cnt += 1
    tot += cnt
    print(cnt, tot)

cnt = tot = 0
dataset = []

while cnt < 100:
    cnt += 1
    if cnt % 3 == 0:
        tot += cnt
        dataset.append(cnt)

print('1 ~ 100 사이 3의 배수 합 = %d' % tot)
print('dataset =', dataset)

# 무한 루프(loop)
numData = []

while True:
    num = int(input("숫자 입력 :"))

    if num % 10 == 0:
        print("프로그램 종료")
        break
    else:
        print(num)
        numData.append(num)

# random
import random
help(random.random)

help(random.random)
10

r = random.random()
print('r=', r)

cnt = 0
while True:
    r = random.random()
    print(random.random())
    if r < 0.01:
        break
    else:
        cnt += 1

print('난수 개수 = ', cnt)



help(random.randint)
help(random.choices)

names = ['홍길동', '이순신', '유관순']
print(names)
print(names[2])

if '유관순' in names:
    print('유관순 있음')
else:
    print('유관순 없음')

idx = random.randint(0, 2)
print(names[idx])

#break, continue
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue
    if i == 6:
        break
    print(i, end=' ')

#for 반복문
string = "홍길동"
print(len(string))
for s in string:
    print(s)

listset = [1, 2, 3, 4, 5]
for e in listset:
    print('원소 :', e)

#range
num1 = range(10)
print('num1 : ', num1)

num2 = range(1, 10)
print('num2 : ', num2)

num3 = range(1, 10, 2)
print('num3 : ', num3)

for n in num1:
    print(n, end = ' ')
print()

for n in num2:
    print(n, end = ' ')
print()

for n in num3:
    print(n, end = ' ')
print()

#for & list
lst = []
for i in range(10):
    r = random.randint(1, 10)
    lst.append(r)

print('lst =', list)

for i in range(10):
    print(lst[i] * 0.25)