# Rules to determine whether a year if leap or not:-
# An year is a leap year if:-
#   a. It is cleanly divisible by 4 - Leap
#   b. Except it is also cleanly divisible by 100 - Not Leap
#   c. Unless it is cleanly divisible by 400 - Leap
year = int(input("Which year do you want to check = "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
