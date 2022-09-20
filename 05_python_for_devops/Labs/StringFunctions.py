# user input for name and stride amount
# apply string stride to user input,
# output alternatiing upper and lower case

while True:
    print("Please type a phrase or group of letters: ")
    userIn = (input())
    len(userIn) <= 26
    if userIn.isalpha() == True:
        userIn = userIn.lower()
        print(f'You entered: {userIn}') 
        break
    
while True:
    print("Please input a number between 1 - 4")
    userStride = int(input())
    if userStride <= 4:
        print(f'You entered: {userStride}')
        break

Answer = []
IncStride = 0
ltrList = list(userIn)
print(ltrList)

while True:
    IncStride <= userStride
    for ltr in ltrList:
        if ltr == ltrList[IncStride]:
            Answer.append(ltr.upper())
            del ltrList[IncStride]
            IncStride += 1
    print(ltrList)
    print(Answer)

# for ltr in ltrList[userStride]:


    #Answer.append[IncStride]
     # IncStride += 1

# for ltr in userIn:
    



# UprIn = userIn[ZeroStride:userStride].upper()

# print(userIn[ZeroStride:userStride].upper())

# print(userIn[::userStride])

# for ltr in userIn(StrideRange):
    # print(ltr)


# for ltr in userIn <= userIn[::userStride]:
    # Uprltr = ltr
     # print(Uprltr)



# for ltr in userIn[::userStride].upper():
    # UprLtr = ltr

# for ltr in userIn[::userStride]:
    # Lowltr = ltr

# print(userIn.replace(Lowltr, UprLtr))

    

# UserStride = userIn[::userStride].upper()
# StrideList = UserStride.split()
# userInList = userIn.split()

# userInList.replace([::userStride], 