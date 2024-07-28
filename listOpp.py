my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]


sum_of_items = sum(my_list)
print("Sum of items:", sum_of_items)


product_of_items = 1
for item in my_list:
    product_of_items *= item
print("Product of items:", product_of_items)


largest_number = max(my_list)
print("Largest number:", largest_number)


smallest_number = min(my_list)
print("Smallest number:", smallest_number)


print("------------------------------------")

print("Question 2")


A = ['abc', 'xyz', 'aba', '1221']

for index in range(len(A)):
    string =  A[index]
    if string[0] == string[-1]:
        print(f"String: {string}, Index: {index}")

print("------------------------------------")
print("Question 3")
string=['A','B','C','D','E']

for i in range(6):
    print(" " * (6 - i), end="")
    for j in range(i):
      print(chr(65 + j), end=" ")
    
    print()


print("\n")
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()

print("-------------------------------------------------")
print("Q4:")

ListColour = ["Black", "Red", "Maroon", "Yellow"]
ListCode = ["000000", "FF0000", "800000", "FFFF00"]

result = [{"colorName": color, "colorCode": code} for color, code in zip(ListColour, ListCode)]

print(result)

print("-------------------------------------------------")
