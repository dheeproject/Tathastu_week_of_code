for i in range(1,9):
    for j in range(1,9):
        if i==j or j==9-i:
            print("*",end="")
        else:
            print(" ",end="")
    print("\n")
