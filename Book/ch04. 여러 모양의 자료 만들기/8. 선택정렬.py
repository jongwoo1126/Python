"""
날짜 : 2022/01/09
이름 : 박종우
내용 : 파이썬 선택 정렬 알고리즘 실습 p106
"""

# 오름차순
dataset = [3, 5, 1, 2, 4]
n = len(dataset)

for i in range(0, n-1):
    for j in range(i+1, n):
        if dataset[i] > dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp

    print(dataset)


print(dataset)

# 내림차순
dataset = [3, 5, 1, 2, 4]
n = len(dataset)

for i in range(0, n-1):
    for j in range(i+1, n):
        if dataset[i] < dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp

    print(dataset)


print(dataset)
