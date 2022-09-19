# user input for name and stride amount
# apply string stride to user input,
# output alternatiing upper and lower case

userIn = ""
userStride = ""

while userIn != str.isalpha:
    print("Please type a phrase or group of letters: ")
    userIn = (input())
    break
else:
    

while userStride != int:
    print("Please input a number between 1 - 4")
    userStride = int(input())
    print("Input can only contain numbers: ")
else:
    pass

userIn = userIn.strip()
for ltr in userIn:
    print(ltr)
    # if ltr == userIn[::userStride]:
        # ltrdict