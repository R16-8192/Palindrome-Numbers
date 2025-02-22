def func(x):
    z = x
    reverse = 0
    while z > 0:
        digit = z % 10
        reverse = reverse * 10 + digit
        z = z // 10
    return x == reverse
y = int(input("Enter Number : "))
if func(y):
    print(f"{y} Is Palindrome")
else:
    print(f"{y} is not Palindrome")
