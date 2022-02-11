input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

result = 0
points = [(1,2), (1,-2), (-1, 2), (-1, -2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
for point in points :
    Row = row + point[1]
    Column = column + point[0]

    print(Row, Column)

    if Row>=1 and Column>=1 and Row<=8 and Column<=8:
        result += 1

print(result)