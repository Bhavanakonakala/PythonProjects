#Ths program verifies whether given number is evn or odd

#Taking user input

num1 = input("what number are you thinking ? ")

# Using if else condition to prove given number is even or odd

if (int(num1) % 2) == 0:
    print("{0} is even".format(num1))
else:
    print("{0} is odd".format(num1))
# Asking the user if they would like to try again
print("Would you like to try again? ")
# Giving options for Yes or No
Yes = '1'
No = '2'
answer = input()
if answer == '1':
    num = input("what number are you thinking ? ")
    if (int(num) % 2) == 0:
        print("{0} is even".format(num))
    else:
        print("{0} is odd".format(num))
else:
    print("Thank you!")

#Done