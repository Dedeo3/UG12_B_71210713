n = int(input("Input : "))
print("Output :")
for y in range(n):
    for v in range(n):
        if v==(n-1) or y==(n-1) or v+y+1==n:
            print("*",end="")
        else:
            print(end=" ")
    print()