# MyFitness Tracker
# Print welcome message to the user.
print("Welcome to Wake n Walk ! ️🚶")
# print options to the user.
print("What would you like to know about ?")
print("1.Track n Walk     "
      "\n2.Track my BMI      "
      "\n3.Track my steps      ")
# Set the input value to option variable.
option = input()
BMI_calculator = '1'
Walking_Tracker = '2'
KM_to_Steps_Calculator  = '3'
if option == '1':
#Get inputs from the user.
    weight = float(input("Please enter your body weight in kg ⚖️ : "))
    distance = float(input("Please enter the target🎯 distance in km : "))
    speed = float(input("Please enter the walking 🚶🚶‍♀️ speed in km/h : "))
# write formula to calculate time in hours and minutes.
# Assign the variables for time in hours and minutes.
    time_in_hours = distance / speed
    time_in_minutes = time_in_hours * 60
    print("It would take {:.2f} hours or {:.2f} minutes ⌚ to walk {:.2f} km at {:.2f} km/h.".format(time_in_hours , time_in_minutes , distance, speed))
# write formula to calculate the number of calories burnt by using user weight,distance and time spent on walking.
    calories_burned = (weight * distance * 1.036) / (time_in_minutes / 60)
    print(f"The number of calories burnt 🔥 are : " , round(calories_burned , 2))
# Calculate BMI
if option == '2':
    weight = float(input("Please enter your body weight in kg ⚖️ : "))
    height = float(input("Please enter your height in cm 📶 : "))
# Write Formula to calculate BMI by using weight and height of the user.
    bmi = (weight / height / height) * 10000
# Use if function to give output to the user.
    if bmi < 18.5:
        print(f"Your BMI is 📝: {bmi:.2f}", "(Underweight ❌)")
        print("Would like to see some diet recommendations for you to gain healthy weight?"
              "\n 1. Yes"
              "\n 2. No")
        answer_diet = input()
        Yes = '1'
        No = '2'
        if answer_diet == '1':
            print("How to put on weight safely"
              "\n1. Eating at least 5 portions of a variety of fruit and vegetables every day. 🍎🥕"
              "\n2. Basing meals on potatoes, bread, rice, pasta. 🥔🍚🍝"
              "\n3. Have whole (full-fat) milk until you build your weight back up. 🥛"
              "\n4. Eating some beans, pulses, fish, eggs, meat and other protein. 🍗🥚"
              "\n5. Drinking plenty of fluids. 🧃🥤")
            print("Thank you! Stay healthy 🙂")
        if answer_diet == '2':
               print("Thank you! Stay Active and Healthy 🙂")
    elif bmi < 25:
        print(f"Your BMI is 📝: {bmi:.2f}", "(Healthy weight ✅)")
        print("Would like to see some diet recommendations for you to lose weight?"
              "\n 1. Yes"
              "\n 2. No")
        answer_diet = input()
        Yes = '1'
        No = '2'
        if answer_diet == '1':
            print("The following are the diet recommendations to maintain healthy weight :"
                  "\n1. Aim for at least five servings of fruits and vegetables a day. 🥕🍎🥗"
                  "\n2. Try and choose whole grain cereal, pasta, rice, and bread. 🍚🍝🍞"
                  "\n3. Avoid food that is high in sugar, like pastries, sweetened cereal, and soda or fruit-flavored drinks. 🍰🧁🍩❌❌❌"
                  "\n4. Reduced-fat or no-fat (skim) milk, reduced-fat cheese, and low-fat or no-fat yoghurt. 🧀")
            print("Thank you! Stay healthy 🙂")
        if answer_diet == '2':
              print("Thank you! Stay Active and Healthy 🙂")
    elif bmi < 30:
        print(f"Your BMI is 📝 : {bmi:.2f}", "(Overweight ⛔)")

        print("Would like to see some diet recommendations for you to lose weight?"
              "\n 1. Yes"
              "\n 2. No")
        answer_diet = input()
        Yes = '1'
        No = '2'
        if answer_diet == '1':
            print("The following are the diet recommendations for you :"
              "\n1. Choose minimally processed, whole foods. "
              "\n2. Whole grains (whole wheat, steel cut oats, brown rice, quinoa). "
              "\n3. Vegetables (a colorful variety-not potatoes)🍅🍆🥕🫑"
              "\n4. Whole fruits 🍇🍉🍊🍎🍑"
              "\n5. Nuts, seeds, beans, and other healthful sources of protein (fish and poultry)🍗🐟."
              "\n6. Plant oils (olive and other vegetable oils)."
              "\n7. Drink water or other beverages that are naturally calorie-free.🥤")
            print("Thank you! Stay Active and Healthy 🙂")
        if answer_diet == '2':
              print("Thank you! Stay Active and Healthy 🙂")
    elif bmi > 30:
        print(f"Your BMI is 📝 : {bmi:.2f}", "(Obesity ❌)")
        print("Would like to see some diet recommendations for you to lose weight?"
              "\n 1. Yes"
              "\n 2. No")
        answer_diet = input()
        Yes = '1'
        No = '2'
        if answer_diet == '1':
            print("The following are the diet recommendations for you :"
              "\n1. Choose minimally processed, whole foods."
              "\n2. Whole grains (whole wheat, steel cut oats, brown rice, quinoa)."
              "\n3. Vegetables (a colorful variety-not potatoes)🍅🍆🥕🫑"
              "\n4. Whole fruits 🍇🍉🍊🍎🍑"
              "\n5. Nuts, seeds, beans, and other healthful sources of protein (fish and poultry)🍗🐟"
              "\n6. Plant oils (olive and other vegetable oils)"
              "\n7. Drink water or other beverages that are naturally calorie-free.")
            print("Thank you! Stay Active and Healthy 🙂")
        if answer_diet == '2':
            print("Thank you! Stay Active and Healthy 🙂")
if option == '3':
# Conversion factor from km to steps
    KM_to_steps = 1312.34
# Input distance in kilometers
    distance_km = float(input("Enter distance in kilometers: "))
# Convert distance to steps
    distance_steps = distance_km * KM_to_steps
# Display the result
    print("It takes {:.2f} steps 👣 to complete {:.2f} distance".format(int(distance_steps) , distance_km))
