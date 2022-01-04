"""
날짜 : 2022/01/03
이름 : 박종우
내용 : 대입연산자
"""

# 변수에 값 할당
i = tot = 10  # i = 10, tot = 10
i += 1  # i= i + 1
tot += i  # tot = tot + i
print(i, tot)

# r같은 줄에 중복 출력
print('출력1', end=' , ')   # end= 구분자
print('출력2')

# 변수 교체
v1, v2 = 100, 200
v2, v1 = v1, v2
print(v1, v2)

#패킹 할당
st1 = [1, 2, 3, 4, 5]
v1, *v2 = st1
print(v1, v2)

*v1, v2 = st1
print(v1, v2)