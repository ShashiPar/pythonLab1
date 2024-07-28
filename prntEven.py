print("Q4:")
def print_even_squares(start, end):

  for num in range(start, end + 1):
    if num % 2 == 0:
      print(f"Number: {num}, Square: {num * num}")

print("---------------1-50---------------")

print_even_squares(1, 50)
print("---------------1-100---------------")
print_even_squares(1, 100)