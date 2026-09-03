# Step 1
str = input("Enter a string: ")
if str == str[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")



# Step 2
def chkPalidromeString(str):
    rev_str = ''
    for char in str:
        rev_str = char + rev_str
    if str == rev_str:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
        