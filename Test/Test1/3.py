"""
날짜 : 2022/01/04
이름 : 박종우
내용 : 파이썬 조건문 연습문제
"""

score = int(input('점수 입력 : '))
grade = None

print('입력한 점수는 %d점 이고, 등급은' % score, end='')

if 100 > score >= 90:
    grade = 'A'
elif 90 > score >= 80:
    grade ="B"
elif 80 > score >= 70:
    grade ="C"
elif 70 > score >= 60:
    grade = "D"
else:
    grade = "F"

print('%s입니다.' % grade)