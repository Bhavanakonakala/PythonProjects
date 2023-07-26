
print("Hello , what is your name ? ")
name = input()
print("Hello " + (name))
print("what you do like to hear? ")
print("1.Joke")
print("2.Riddle")
Joke = '1'
Riddle = '2'
answer = input()
if answer == '1':
    print("What has four wheels and flies? "
          "Garbage truck.")
if answer == '2':
    print("What can run but can't walk?")
    answer1 = input()
    if answer1 == 'River':
        print("Congartulations!!! You are right.")
    else:
        print("No! Its a River.")
        print("Yay I won!!!")


