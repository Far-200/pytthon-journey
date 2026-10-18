print("Palindrome Program")
num = int(input("Enter a number: "))
og = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = (reverse * 10) + digit
    num //= 10
if(reverse == og):
    print("Palindrome!")
else:
    print("Not Palindrome!")
print(og)
print(reverse)