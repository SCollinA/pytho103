ERROR_MESSAGE = "User did not input number 0-6"
# Fill in your code here
try:
    day = int(input('Day (0-6)? '))
    if day > 0 and day < 6:
        print("Go to work")
    elif day == 0 or day == 6:
        print("Sleep in")
    else:
        print(ERROR_MESSAGE)
except:
    print(ERROR_MESSAGE)