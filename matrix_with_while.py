mat1 = []
mat2 = []
while True:
    number1 = input("Enter Number Of Matrix1 :")
    if number1 == '*':
        while True:
            number2 = input("Enter Number Of Matrix2:")
            if number2 == '=':
                print("Matrix 1 :")
                for i in range(len(mat1)):
                    for j in range(len(mat1[i])):
                        print(mat1[i][j],end=" ")
                    n = len(mat1)
                    m = len(mat1[i])
                    print()
                print("Matrix 2 :")
                for i in range(len(mat2)):
                    for j in range(len(mat2[i])):
                        print(mat2[i][j],end=" ")
                    k = len(mat2)
                    l = len(mat2[i])
                    print()
                print(n ,"-", m ,"-", k ,"-",l)
                print("Result :")
                if m == k :
                    result= [[0 for i in range(l)] for j in range(n)]
                    for x in range(n):
                        for y in range(l):
                            for z in range(m):
                                result[x][y]+=mat1[x][z]*mat2[z][y]
                    for i in range(n):
                        for j in range(l):
                            print(result[i][j],end=" ")
                        print()
                else:
                    print("Error , Because column of matrix1 not equal row of matrix2 !!!")
                break
            else:
                list2=number2.split()
                list2 = [int(item) for item in list2]
                mat2.append(list2)
        break
    else:
        list1=number1.split()
        list1 = [int(item) for item in list1]
        mat1.append(list1)
