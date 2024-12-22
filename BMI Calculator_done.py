#Author:Ricardo Medero
#Date Create:02/13/24 update 02/21/2024
#BMI Calculator

#Contant
METERS = 39.36
KILOGRAMS = 2.2

#print, String, float input
print("Welcome to Ricardo` BMI Calculator!")

sName = input("Name of the person we are calculating the BMI for:")

#input in float them make logic conversion from Inches to Meters in one line
fHeight = float(input("Supply Height in Inches: "))/METERS

#input in float them make logic conversion from pounds to kilograms in one line
fWeight = float(input("Supply Weight in Pounds: ")) / KILOGRAMS

#Logic calculation the BMI
fBMI = fWeight / (fHeight * fHeight)

#Output name and BMI alredy calculate with 2 demcimal number
print(f"{sName} BMI is: {fBMI:,.2f}")

#Logical Stament

if fBMI >= 29.90:
    print("BMI the finding is:Obese")
elif fBMI >= 24.90:
    print("BMI the finding is: Overweight")
elif fBMI >= 18.51:
    print("BMI the finding is: Normal")
else:
    print("BMI the finding is: Underweight")

