#Compound Interest
#Author Ricardo Medero
#Create: 02/12/24 update 02/15/24

#Variable, float, int and input
#Principal Value is the starting amount.

fPrincipleValue =  float(input("Enter the starting principal:  "))

#interest rate input in float divide by 100
fInterestRate = float(input("Enter the annual interest rate:  "))/100

#Compounding input  in float
fCompoundPerYear = float(input("How many times per year is interest compounded? "))


#NumberofPeriods input in int
iYears = int(input("For how many years will the account earn interest? "))


#Logic Calculation

fResult = fPrincipleValue * (1 + fInterestRate / fCompoundPerYear) ** (fCompoundPerYear * iYears)

#Result Ouput in fast string the time account earning and the Result in float with format 2 decimal point

print(f"At the end of {iYears} year you will have ${fResult:,.2f}")
















