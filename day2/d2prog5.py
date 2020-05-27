n=3
for i in range(n,0,-1):
    print(i,end="")
    for j in range (i-1):
        print("*",i,end="")
    print("\n")
for i in range(1,4,+1):
    k=i
    print(i,end="")
    for j in range(1,i):
        print("*",i,end="")
    print("\n")
