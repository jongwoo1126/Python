"""
날짜 : 2022/02/18
이름 : 박종우
내용 : 코딩테스트 선택정렬 실습
"""

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):

    for j in range(i+1, len(array)):

        if array[i] > array[j]:

            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp


print(array)