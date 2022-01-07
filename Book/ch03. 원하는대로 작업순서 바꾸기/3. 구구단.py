"""
날짜 : 2022/01/06
이름 : 박종우
내용 : 구구단 p74
"""

for i in range(2, 10):
    print('~~~ {}단 ~~~'.format(i))

    for j in range(1, 10):
        print('%d * %d = %d' % (i, j, i*j))