def isPalindrome(x):
    if x < 0:
      return False  
    a = x
    reverse = 0
  
    while x > 0:
      digit = x % 10
      reverse = reverse * 10 + digit
      x //= 10
        
    return a == reverse
inp = int(input("Enter Number : ")
if isPalindrome(inp):
    print("Is palindrome")
else:
    print("Is not palindrome")
