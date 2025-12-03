matrixLen = int(input('enter the len: '))

rowfor2 = []
rowfor3 = []
colfor2 = []
colfor3 = []
anothercolfor3 = []

if matrixLen == 2:
    for i in range(2):
        row = int(input(f'enter {i+1} column: '))
        rowfor2.append(row)
        column = int(input())
        colfor2.append(column)

    print("this is your matrix")
    print(f'''
[{rowfor2[0]}  {rowfor2[1]}]
[{colfor2[0]}  {colfor2[1]}]
''')

    print("transpose matrix be like this")
    print(f'''
[{rowfor2[0]}  {colfor2[0]}]
[{rowfor2[1]}  {colfor2[1]}]
''')

    print('flatten of the matrix')
    print(f'''
[{rowfor2[0]}, {rowfor2[1]}, {colfor2[0]}, {colfor2[1]}]
''')

elif matrixLen == 3:
    for i in range(3):
        row = int(input(f'enter {i+1} column: '))
        rowfor3.append(row)
        column = int(input())
        colfor3.append(column)
        col = int(input())
        anothercolfor3.append(col)

    print("this is your matrix")
    print(f'''
[{rowfor3[0]}  {rowfor3[1]}  {rowfor3[2]}]
[{colfor3[0]}  {colfor3[1]}  {colfor3[2]}]
[{anothercolfor3[0]}  {anothercolfor3[1]}  {anothercolfor3[2]}]
''')

    print("transpose matrix be like this")
    print(f'''
[{rowfor3[0]}  {colfor3[0]}  {anothercolfor3[0]}]
[{rowfor3[1]}  {colfor3[1]}  {anothercolfor3[1]}]
[{rowfor3[2]}  {colfor3[2]}  {anothercolfor3[2]}]
''')

    print('flatten of the matrix')
    print(f'''
[{rowfor3[0]}, {rowfor3[1]}, {rowfor3[2]}, 
 {colfor3[0]}, {colfor3[1]}, {colfor3[2]}, 
 {anothercolfor3[0]}, {anothercolfor3[1]}, {anothercolfor3[2]}]
''')

else:
    print('it is under process')
