#This program shows if the given string is palindrome or not
def palindrome(string):
    if(string == string[::-1]):
        return "The given word is palindrome!"
    else:
        return "The given word is not palimdrome!"
string = input("Please enter a word :")
print(palindrome(string))