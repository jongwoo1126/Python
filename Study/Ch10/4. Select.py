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
sql = "SELECT * FROM `User1`;"
cur.execute(sql)
conn.commit()

#데이터 출력
dataset = cur.fetchall()
#print(dataset)
for row in dataset:
    print('=====================')
    print('아이디 : ', row[0])
    print('이름 : ', row[1])
    print('휴대폰 : ', row[3])
    print('나이 : ', row[3])
    print('---------------------')

# 데이터베이스 종료
conn.close()

print("Select 완료...")