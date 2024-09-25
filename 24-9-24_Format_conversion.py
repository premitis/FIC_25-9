# Palindrome check
def check_str_palindrome(str):
    if str == str[::-1]:
        print(f"string provided : {str}, is a palindrome !")
    else:
        print(f"{str} IS not a palindrome :(")
        
check_str_palindrome("racecar")
check_str_palindrome("A")
check_str_palindrome("BA")
check_str_palindrome("ABA")
check_str_palindrome("ABBA")
#comment