def find_sum_and_reverse(number):
  sum_of_digits = 0
  reverse = 0
  temp = number

  while temp > 0:
    digit = temp % 10
    sum_of_digits += digit
    reverse = reverse * 10 + digit
    temp //= 10

  return sum_of_digits, reverse


number = int(input("Enter a four-digit number: "))


sum, reverse = find_sum_and_reverse(number)

print("Sum of digits:", sum)
print("Reverse:", reverse)