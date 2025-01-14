def is_palindrome(s):
    return s == s[::-1]

s = "malayalam"
ans = is_palindrome(s)

if ans:
    print("Yes")
else:
    print("No")