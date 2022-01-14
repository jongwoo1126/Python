"""
날짜 : 2022/01/03
이름 : 박종우
내용 : 문자열 (String)
"""

# 문자열 유형
oneLine = "this is one line string"
print(oneLine)

multiLine = """this is
multi line
string"""
print(multiLine)

multiLine2 = "this is\nmulti line\nstring"
print(multiLine2)

# 문자열 색인
string = "PYTHON"
print(string[0])
print(string[5])
print(string[-1])
print(string[-6])

# 문자열 연산
print("PYTHON" + "PROGRAM")
print("PYTHON-" + str(3.7) + ".exe")
print("-"*30)

# 슬라이싱
print(oneLine)
print("문자열 길이 : ", len(oneLine))
print(oneLine[0 : 4])
print(oneLine[ : 4])
print(oneLine[ : ])      # 전체 원소
print(oneLine[::2])      # 2의 배수 index

print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])

subString = oneLine[-11:]
print(subString)

# 특정 글자 수 반환
oneLine = 'this is one line string'
print('t 글자수 :', oneLine.count('t'))
print('i 글자수 :', oneLine.count('i'))

# 접두어 문자 비교
print(oneLine.startswith('this'))
print(oneLine.startswith('that'))

# 문자열 교체
print(oneLine.replace('this', 'that'))

# 문자열 분리 (문단 -> 문장)
multiLine = """this is
multi line
string"""
sent = multiLine.split('\n')
print('문장 :', sent)

# 문자열 분리 (문장 -> 단어)
words = oneLine.split(' ')
print('단어 :', words)

# 문자열 결합 (단어 -> 문장)
sent2 = ','.join(words)
print(sent2)

# escape 문자 적용
print('escape 문자 차단')
print('\n출력 이스케이프 문자')

# escape 문자 기능 차단
print('\\n출력 이스케이프 기능 차단1')
print(r'\n출력 이스케이프 기능 차단2')

# 경로 표현 : C:\Python\test
print('path =', 'C:\Python\test')
print('path =', 'C:\\Python\\test')
print('path =', r'C:\Python\test')