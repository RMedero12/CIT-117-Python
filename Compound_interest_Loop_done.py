#Compound Interest Loops
#Author Ricardo Medero
#Created 2/20/24 updated 2/24/24
#Contants
MINVALUE = 0
NEGATIVEVALUE = -1

#Defined Name
fOriginalDeposit = 0
fInterestRate = 0
iNumberofMonth = 0
fGoal = -1
#Logic loops only accept number mus be positive no characters
while fOriginalDeposit <= MINVALUE:
    try:
        fOriginalDeposit = float(input("What is the Original Deposit (positive value):"))

    except ValueError:
        print("Must be positive Numerical value")


#Logic loops for Months and calculation interest Rate divide 100 and
#Year divide by 12 to get monthly
while fInterestRate <= MINVALUE:
    try:
        fInterestRate = float(input("What is the Interest Rate (positive value):"))
        fYear = fInterestRate/100
        fMonthly = fYear/12

    except ValueError:
        print("Must be positive Numerical value")


#print(f"Monthly rate: {fMonthly:}")


while iNumberofMonth <= MINVALUE:
    try:
        iNumberofMonth = int(input("What is the Number of Months (positive value):"))

    except ValueError:
        print("Must be positive Numerical value")

#Logic loops for Goal with true and false staments

while fGoal <= NEGATIVEVALUE:
    try:
        fGoal = float(input("What is the Goal Amount (can enter 0 but no negative ):"))

    except ValueError:
        print("Must be positive Numerical value")

    if fGoal < MINVALUE:
            print("Input must 0 or greater ")




Balance = fOriginalDeposit


for Month in range(1, iNumberofMonth + 1):
    fMonthlyAmount = fMonthly * Balance
    Balance += fMonthlyAmount
    print(f"Month:  {Month}  Account Balance is : ${Balance:,.2f}")



while Balance < fGoal:
    fMonthlyAmount = fMonthly * Balance
    Balance += fMonthlyAmount
    iNumberofMonth += 1


#logic if stament to determinate if user input 0 or Number of Month.
if fGoal <= 0:
    iNumberofMonth = 0

print(f"It will take: {iNumberofMonth} Months to reach your goal of ${fGoal:,.2f}")













