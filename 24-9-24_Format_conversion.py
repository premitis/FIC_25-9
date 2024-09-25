# Palindrome check
def check_str_palindrome(str):
    if str == str[::-1]:
        print(f"YAY!, string {str} is Palindrome!!")
    else:
        print(f"Sorry, string {str} is not a Palindrome :(")
        
check_str_palindrome("racecar")
