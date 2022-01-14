"""
날짜 : 2022/01/07
이름 : 박종우
내용 : 비순서 자료구조 Set
"""

# 중복 불가
s = {1, 3, 5, 3, 1}
print(len(s))
print(s)

# 요수 반복
for d in s:
    print(d, end=' ')

print()

# 집합관련 함수
s2 = {3, 6}
print(s.union(s2))  # 합집합
print(s.difference(s2))  # 차집합
print(s.intersection(s2))  # 교집합

# 추가, 삭제 함수
s3 ={1, 3, 5}
print(s3)

s3.add(7)
print(s3)

s3.discard(3)
print(s3)

# 중복제거
gender = ['남', '여', '남', '여']

sgender = set(gender)
lgender = list(sgender)
print(lgender)

print(lgender[1])