"""
날짜 : 2022/01/03
이름 : 박종우
내용 : 표준입출력장치
"""

#표준입력장치
#(1) 문자형 숫자 입력
num = input('숫자 입력 : ')
print('num type : ', type(num))
print('num = ', num)
print('num = ', num*2)

#(2) 문자형 숫자를 정수형으로 변형
num1 = int(input('숫자 입력 : '))
print('num1 = ', num1*2)

#(3) 문자형 숫자를 실수형으로 변환
num2 = float(input("숫자 입력 : "))
result = num1 + num2
print('result = ', result)


#표준출력장치
#(1) value 인수
print("value = ", 10 + 20 + 30 + 40 + 50)

#(2) sep 인수
print('010', '1234', '5678', sep="-")

#(3) end 인수
print("value = ", 10, end = ", ")
print("value = ", 20)

# format
print("원주율 = ", format(3.141592), "8.3f")
print("금액 = ", format(1000,"10d"))
print("금액 = ", format(125000, "3,d"))

# 양식문자 인수
name = "홍길동"
age = 35
price = 123.456
print("이름 : %s, 나이 : %d, data = %.2f" %(name, age, price))

# 외부 상수 인수
print("이름 : {}, 나이  : {}, data={}".format(name, age, price))

# format 축약형
uid = input("id input : ")
query = f"select * from member where uid = {uid}"
print(query)