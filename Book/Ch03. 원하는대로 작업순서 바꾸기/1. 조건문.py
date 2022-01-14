"""
날짜 : 2022/01/04
이름 : 박종우
내용 : 조건문
"""

# 단일 조건문
var = 10

if var >= 5:
    print('var =',var)
    print('var는 5보다 크다.')
    print('조건이 참인 경우 실행')

print('항상 실행')

score = int(input('점수 입력 : '))
if 100 >= score >= 85:
    print('우수')
elif 84 >= score >= 70:
    print('보통')
else:
    print('저조')

# 중첩 조건문
score = int(input('점수 입력 :'))
grade = ''

if 100 >= score >= 85:
    grade = '우수'
elif score >= 70:
    grade = '보통'
else:
    grade = '저조'

print('당신의 점수는 %d이고, 등급은 %s' % (score, grade))

# 삼항 조건문

num = 9
result = 0

if num >= 5:
    result = num * 2
else:
    result = num + 2
print('result =', result)

result2 = num * 2 if num >= 5 else num + 2
print('result2 =', result2)