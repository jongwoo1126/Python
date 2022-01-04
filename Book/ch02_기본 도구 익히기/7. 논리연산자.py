"""
날짜 : 2022/01/03
이름 : 박종우
내용 : 논리연산자
"""

# 두 관계식이 같은지 판단
num1 = 100
num2 = 20

log_result = num1 >= 50 and num2 <= 10
print(log_result)

# 두 관계식 중 하나라도 같은지 판단
log_result = num1 >= 50 or num2 <= 10
print(log_result)

log_result = num1 >= 50  # 관계식 판단
print(log_result)

# 괄호 안의 관계식 판단 결과에 대한 부정
log_result = not(num1 >= 50)
print(log_result)