num = int(input("Enter a positive integer: "))

original = num
sum_digits = 0
count = 0
reverse = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    count += 1
    reverse = reverse * 10 + digit
    num //= 10

print("Original Number:", original)
print("Sum of Digits:", sum_digits)
print("Number of Digits:", count)
print("Reversed Number:", reverse)