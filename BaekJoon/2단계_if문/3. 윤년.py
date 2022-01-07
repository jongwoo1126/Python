year = int(input())
year1 = year % 4 == 0 and  year % 100 !=0 or year % 400 == 0

if year1:
    print(1)
else:
    print(0)