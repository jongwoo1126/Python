"""
날짜 : 2022/01/07
이름 : 박종우
내용 : 자료구조 Tuple
"""

# 원소 한개
t = (10,)
print(t)

# 원소 여러개
t2 = (1, 2, 3, 4, 5, 3)
print(t2)

# 튜플 색인
print(t2[0], t2[1:4], t2 [-1])

# 수정 불가
# t2[0] = 10 # Error

# 요소 반복
for i in t2:
    print(i, end=' ')

# 요소 검사
if 6 in t2:
    print('6 있음')
else:
    print('6 없음')

# 튜플 자료형 변환
lst = list(range(1, 6))
t3 = tuple(lst)
print(t3)

# 튜플 관련 함수
print(len(t3), type(t3))
print(t3.count(3))
print(t3.index(4))