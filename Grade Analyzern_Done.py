# welcome to Grade Analyzer
#Author:Ricardo Medero
#Creater:02/15/2024 updated:02/19/2024


print("Welcome to Grade Analyzer!")

sName = input("Name of the person we are calculating the grade for: ")

#Grade of each Test in input int
iTest1 = int(input("Test1 Grade: "))
iTest2 = int(input("Test2 Grade: "))
iTest3 = int(input("Test3 Grade: "))
iTest4 = int(input("Test4 Grade: "))
# if stament to make sure scores are not less then zero but can be zero
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test must be greater than  0.")
    exit(0)

#string input fom the user must be Yes or No
strDrop = (input("Do you wish to Drop the Lowest Grade Y or N? ")).upper()

#the string input if the condition is NO will make calculation and print the result
if strDrop == "N":
    fAverage = (iTest1 + iTest2 + iTest3 + iTest4) / 4

#if the condition is Yes them the code will determinate wich grade is lower and drop from the calculation
#them output the average

elif strDrop == "Y":

    if iTest1 < iTest2 and iTest1 < iTest3 and iTest1 < iTest4:

        fAverage = (iTest2 + iTest3 + iTest4) / 3

    elif iTest2 < iTest3 and iTest2 < iTest4:

        fAverage = (iTest1 + iTest3 + iTest4) / 3

    elif iTest3 < iTest4:

        fAverage = (iTest1 + iTest2 + iTest4) / 3

    else:

        fAverage = (iTest1 + iTest2 + iTest3) / 3

#else stament for if the user type diferent character that is not Y or N
else:
    print("Enter Y or N to drop the lowest grade")
    exit()




#if staments after the Averange logic is done will determinate what letter grade is.

if fAverage >= 97.0:
    sGrade = "Your letter grade for the test is: A+"

elif fAverage >= 94.0:
    sGrade = "A"

elif fAverage >= 90.0:
    sGrade = "A-"

elif fAverage >= 87.0:
    sGrade = "B+"

elif fAverage >= 84.0:
    sGrade = "B"

elif fAverage >= 80.0:
    sGrade = "B-"

elif fAverage >= 77.0:
    sGrade = "C+"

elif fAverage >= 74.0:
    sGrade = "C"

elif fAverage >= 70.0:
    sGrade = "C-"

elif fAverage >= 67.0:
    sGrade = "D+"

elif fAverage >= 64.0:
    sGrade = "D"

elif fAverage >= 60.0:
    sGrade = "D-"
else:
    sGrade = "F"
# output in fast str variable name input from the user and Average formating in one decimal point.
#and new line for grade
print(f"{sName} test average is {fAverage:.1f}\nYour letter grade for the test is: {sGrade}")
