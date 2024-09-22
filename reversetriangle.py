
''' for printing revers rifht triangle '''




for i in range(11):
    for j in range(10-i):
        print("*",end="")
        print()

''' for print the proper left triangle '''
for i in range(11):
    i=i-1
    for j in range(i):
        print("*",end="")


    print()

''' printing proper middle tiangle ''' 
n = 4
for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")

        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()


