"""
날짜 : 2022/01/09
이름 : 박종우
내용 : 자료구조 복제 교제 p102
"""

# 얕은 복사 : 주소 복사
name = ['홍길동', '이순신', '강감찬']
print('name addres =', id(name))

name2 = name
print('name2 address =', id(name2))

print(name)
print(name2)

# 원본수정
name2[0] = "김길동"
print(name)
print(name2)

# 깊은 복사
import copy
name3 = copy.deepcopy(name)
print(name)
print(name3)
print('name addres =', id(name))
print('name3 addres =', id(name3))

#원본 수정
name[1] = "이순신장군"
print(name)
print(name3)