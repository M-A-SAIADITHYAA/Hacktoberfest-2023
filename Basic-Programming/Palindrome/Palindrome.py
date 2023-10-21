intd =input("Enter the integer")
def palindrome(intd):
    gav = intd[::-1]
    if gav == intd:
        return True
    else:
        return False
result = palindrome(intd)
print(result)