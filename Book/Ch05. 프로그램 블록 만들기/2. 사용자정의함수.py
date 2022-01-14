"""
날짜 : 2022/01/09
이름 : 박종우
내용 : 파이썬 사용자정의함수 실습 p123
"""

# 인수가 없는 함수
def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')

userFunc1()    # 함수 호출

# 인수가 있는 함수
def userFunc2(x, y):
    print('userFunc2')
    z = x + y
    print('z = ', z)

userFunc2(10, 20)

#return 있는 함수
def userFunc3(x, y):
    print('userFunc3')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return tot, sub, mul, div

x = int(input('x 입력 : ', ))
y = int(input('y 입력 : ', ))

t, s, m, d = userFunc3(x, y)
print('tot =', t)
print('sub =', s)
print('mul =', m)
print('div =', d)