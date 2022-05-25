A = input()
list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

t = 0

for i in list :
    for j in i :
        for k in A :
            if k == j :
                t += list.index(i) + 3

print(t)