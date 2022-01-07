a = [0 ,10, 20, 30, 40, 50, 60, 70]
print(a[:7:2])


string = input('7문자 이상 문자열 입력 :')
m1 = string[1:3] + string[-1:]
m2 = string[:3] + string[-3:-1]
m3 = string[0:3] + string[-3:]
m4 = string[0:] + string[:-1]
print(m1)
print(m2)
print(m3)
print(m4)