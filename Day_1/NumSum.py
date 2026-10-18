print ("Something")

num = int(input("Enter a number: "))
digit_sum = 0
og = num
while num > 0:
    digit = num % 10
    digit_sum += digit
    num //= 10
print(og)
print("\n")
print(int(digit_sum))