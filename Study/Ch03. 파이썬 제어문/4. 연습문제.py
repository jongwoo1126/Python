"""
날짜 : 2022/01/03
이름 : 박종우
내용 : 파이썬 반복문 for 실습하기 교재 p70
"""

"""[문제1]"""
"""[문제2] while 반복문을 이용한 '숫자 맞추기 게임'"""
import random

print('>>숫자 맞추기 게임<<')
com = random.randint(1, 10)    #1 ~ 10 사이 난수 정수 발생

while True :
    my = int(input('예상 숫자를 입력하시오 :'))   #숫자 입력

    if com == my:
        print('~~성공~~')
        break
    if com < my:
        print ('더 작은 수 입력')
        continue
    if com > my:
        print('더 큰 수 입력')
        continue

"""[문제3]"""
"""[문제4]"""