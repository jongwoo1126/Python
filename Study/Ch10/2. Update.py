"""
날짜 : 2022/01/13
이름 : 박종우
내용 : 파이썬 데이터베이스 프로그래밍 실습하기 교재 P295
"""
import pymysql

# 데이터베이스 실행
conn = pymysql.connect(host='54.180.160.240',
                       user='lucky4527',
                       password='1234',
                       db='lucky4527',
                       charset='utf8')

# SQL 실행객체 생성
cur = conn.cursor()

# SQL 실행
sql = "UPDATE `User1` SET `age` = `age`+1 WHERE `uid`='p101';"
cur.execute(sql)
conn.commit()

# 데이터베이스 종료
conn.close()

print("Update 완료....")