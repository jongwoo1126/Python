A = input()
list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in list:
    A = A.replace(i,'*')

print(len(A))

