def check_palindrome(string):
    if len(string) == 1:
        return string
    else:
        return  check_palindrome(string[1:]) + string[0]
    
string = "radar"
string = ''.join(letter for letter in string if letter.isalnum())

print(string == check_palindrome(string))

