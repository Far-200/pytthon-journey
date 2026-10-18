print("Reversing Number")
num = int(input("Enter a number: "))
og = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num //= 10

print(og)
print(reverse)