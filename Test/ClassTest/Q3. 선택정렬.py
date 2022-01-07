"""
날짜 : 2022/00/00
이름 : 박종우
내용 : 파이썬 선택 정렬 알고리즘
"""
dataset = [3, 5, 1, 2, 4]
n = len(dataset)

for i in range(0, n-1):
    for j in range(i+1, n):
        if dataset[i] > dataset[j]:
            tmp = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = tmp

    # 각 회전 정렬 내용
    print(dataset)

# 최종 정렬 내용
print(dataset)