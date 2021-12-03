n = int(input("Masukkan banyak bilangan : "))
i = 1

print("Total = ", end="")

for z in range(1, n + 1):
    if z % 7 == 0:
        i = i + 0
        print("+ 0", end=" ")
    elif z % 3 == 0:
        i = i + (z * -1)
        print("- " + str(z), end=" ")
    elif z == 1:
        print(str(z), end=" ")
    else:
        i = i + z
        print("+ " + str(z), end=" ")

print("\nHasil perhitungan diatas ialah " + str(i))