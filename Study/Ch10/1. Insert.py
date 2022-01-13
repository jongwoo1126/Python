"""
날짜 : 2022/01/13
이름 : 박종우
내용 : 파이썬 데이터베이스 프로그래밍 실습하기 교재 P295
"""

import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='54.180.160.240',
                       user='lucky4527',
                       password='1234',
                       db='lucky4527',
                       charset='utf8')

# SQL실행 객체 생성(Cursor)
cur = conn.cursor()

# SQL실행
sql = "INSERT INTO `User1` VALUES ('p101', '정약용', '010-1212-1010', 43);"
cur.execute(sql)
conn.commit()

# 데이터베이스 종료
conn.close()

print('Insert 완료...')