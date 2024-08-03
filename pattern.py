for i in range(6):
    print(" " * (6 - i), end="")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()
