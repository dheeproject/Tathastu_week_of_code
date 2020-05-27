n=5
for i in range(n):
    print("*" * (n-i) + " " *(2*i+1)+"*"*(n-i))
for i in range(n,0,-1):
    print("*" * (n-i+1) + " " * (i*2-1) + "*" * (n-i+1))
    
