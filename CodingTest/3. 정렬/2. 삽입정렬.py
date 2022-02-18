"""
날짜 : 2022/02/18
이름 : 박종우
내용 : 코딩테스트 삽입정렬 실습
"""
import time

start_time = time.time()

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):

    for j in range(i, 0, -1):

        if array[j] < array[j-1]:

            tmp = array[j-1]
            array[j-1] = array[j]
            array[j] = tmp
        else:
            break
print(array)

end_time =time.time()
total_time = end_time-start_time
print('수행시간 :', total_time)