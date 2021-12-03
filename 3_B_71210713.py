kata1 = str(input("Input :"))
length = len(kata1)
print("Output :")
for i in range(length):
    for j in range(length-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print(kata1[j],end=" ")
    print()
for i in range(length):
    for j in range(i):
        print(" ",end=" ")
    for j in range(length-i):
        print(kata1[j],end=" ")
    print()