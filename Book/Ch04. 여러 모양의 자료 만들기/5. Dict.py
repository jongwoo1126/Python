"""
날짜 : 2022/01/07
이름 : 박종우
내용 : 비순서 자료구조 Dict
"""

# dict  생성 방법
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic)

person = {'name':'홍길동', 'age':35, 'address':'서울시'}
print(person)
print(person['name'])
print(type(dic), type(person))

# 원소 수정, 삭제, 추가
person['age'] = 45
print(person)

# 원소 삭제
del person['address']
print(person)

# 원소 추가
person['pay'] = 350
print(person)

# 요소검사와 반복
print(person['age'])
print('age' in person)

for key in person.keys():
    print(key)
for v in person.values():
    print(v)
for i in person.items():
    print(i)

# 단어 빈도수
charset = ['abc', 'code', 'band ', 'band', 'abc']
wc = {}

for key in charset:
    wc[key] = wc.get(key, 0) + 1
    print(wc)