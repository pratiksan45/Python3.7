def palindrome(a):
    if a == a[::-1]:
        return True
    else:
        return False
string=input("Enter The string\n")
print(palindrome(string))

