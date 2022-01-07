"""
날짜 : 2022/01/07
이름 : 박종우
내용 : 자료구조 List
"""
# 단일 리스트
lst = [1, 2, 3, 4, 5]
print(lst)
print(type(lst))

for i in lst:
    print(lst[:i])

# 단일 list 색인
x = list(range(1, 11))
print(x)
print(x[:5])
print(x[-5:])
print('index 2씩 증가')
print(x[::2])   #홀수 색인인
print(x[1::2])  # 1부터 시작하는 짝수 색인

# 중첩 리스트 객체
a = ['a', 'b' ,'c']
print(a)

b = [10, 20, a, 5, True, '문자열']
print(b[0])
print(b[2])
print(b[2][0])
print(b[2][1:])

# 추가, 삭제, 수정, 삽입
num = ['one', 'two', ' three',' four']
print(num)
print(len(num))

num.append('five')
print(num)

num.remove('five')
print(num)

num[3]= '4'
print(num)

num.insert(0,'zero')
print(num)

x = [1, 2, 3, 4]
y = [1.5, 2.5]
z = x + y
print(z)

x.extend(y)
print(x)

x.append(y)
print(x)

lit = [1, 2, 3, 4]
result = lst * 2
print(result)

# 리스트 정렬과 요소 검사
print(result)
result.sort()
print(result)
result.sort(reverse = True)
print(result)

import random
r = []
for i in range(5):
    r.append(random.randint(1, 5))

print(r)
if 4 in r:
    print('있음')
else:
    print('없음')

x = [2, 4, 1, 5, 7]

lst = [i ** 2 for i in x] # 변수 = [실행문 for]
print(lst)

num = list(range(1, 11))
lst2 = [i*2 for i in num if i % 2 == 0]  # 변수 = [실행문 for if]
print(lst2)