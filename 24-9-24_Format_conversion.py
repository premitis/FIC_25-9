# Palindrome check
def check_str_palindrome(str):
    if str == str[::-1]:
        print(f"string provided : {str}, is a palindrome !")
    else:
        print(f"{str} is not a palindrome :(")
        
check_str_palindrome("racecar")
