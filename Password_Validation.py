#Author:Ricardo Medero
#Date: 10/2/24

#funtion to get the initials with list index to get the initials
def getName(sName):
    sInitials = sName[0] + sName[sName.find(" ") + 1]
    return sInitials

#funtion to check the leng of the password and dont start with pass or Pass with loop to try again,
#if they dont meet the criterial

def getPassword(sPassword):
    while True:
        UserInput = input(sPassword)
        if len(UserInput) >=8 and len(UserInput) <=12:
            if UserInput.lower().startswith("pass"):
                print("Password cant contain Pass or pass")

                continue
            else:
                return UserInput
        else:
            print("Password must be at least 8 and 15 characters")

#funtion to check if all the criterial are meet for validate the password.
def getPassWordValidation(sInitial, sPassword):
            dictRep = {}
            bInitials = True
            bNumeric = False
            bLower = False
            bUpper = False
            bSpecialList = False
            bRepeatedCharacter = False

# using loop for verify if password criterial are meet through boolean expression
            for char in sPassword:
                if sInitial in sPassword.upper():
                    bInitials = False
                if char.isnumeric():
                    bNumeric = True
                if char.islower():
                    bLower = True
                if char.isupper():
                    bUpper = True
                if char in '! @ # $ % ^':
                    bSpecialList = True
#using dictionary for verify if character are repeated in the password
                RepeatedChar = sPassword.lower().count(char.lower())
                if RepeatedChar > 1:
                    bRepeatedCharacter = True
                    dictRep[char.lower()] = RepeatedChar

#if one of the condition don`t meet one of the criterial will print to the screen.

            if bInitials == False:
                print("Password must not contain user initials")
            if bLower == False:
                print("Password must contain at least 1 lowercase characters")
            if bUpper == False:
                print("Password must contain at least 1 uppercase characters")
            if bNumeric == False:
                print("Password must contain at least 1 numeric characters")
            if bSpecialList == False:
                print("Password must contain at least 1 special characters")
            if bRepeatedCharacter == True:
                print(f"This Character has been repeated{dictRep}")

#if all the condition meet the criterial will return accepted

            if bLower and bUpper and bNumeric and bSpecialList and bInitials == True and bRepeatedCharacter == False:
                 return "Acepted"

def main():
#loop for if one of the criteria is not meet start again.
# if the user on Sname dont input letter going to continue on loop.
    while True:
        sName = input("Enter your first name and Lastname: ")
        sInitial = getName(sName)
        if not sInitial.isalpha():
            continue

        sPassword = getPassword("Enter password: ")
        sValidation = getPassWordValidation(sInitial, sPassword)
        if sValidation == "Acepted":
            print("Your password is valid")
            break

#Acepted is going to return on sValidation if return acepted will print to the screen







main()