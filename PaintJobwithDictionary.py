#Paint Jobs with functions and dictionary
#Author: Ricardo Medero
#Create:03/15/24 update 4/24/24
import math
# dictionary for the State tax the key is the State and the value is the numbers.
dict_TAX_RATES = {
        "CT": 0.06,
        "VT": 0.06,
        "MA": 0.0625,
        "ME": 0.0625,
        "RI": 0.07,

    }
#define funtion for ask to the user SquareFeet, HoursofLabor, FeetperGallon, HourperGallon and LaborChargeHours
#with loop for validate the user input.
UserInput = 0
def getFloatInput(sPrompt: str, fMinAllowedValue: float) -> float:
    while UserInput <= fMinAllowedValue:
        try:
            nUserInput = float(input(sPrompt))
        except ValueError:
            print("Not a valid number! Please try again.")
            continue

        else:
            if nUserInput < fMinAllowedValue:
                print("Entry must be greater than or equal to", fMinAllowedValue, ", Please try again.")
            else:
                return nUserInput


#define function for get the value in the dictionary and return to use in diferent funtion
#if the user input is not in the dictionary will be return 0.
def getStateTax(sState):
    if sState in dict_TAX_RATES:
       return dict_TAX_RATES[sState]
    else:
        return 0
#define funtion for know how many gallon will be use , divide by squarefeet and feetpergallon
#them using math module imported in line 4 for use math.cel() for round up to near integer
def getGallonofPaint(fSquareFeet, fFeetperGallon) -> float:
    iGallonofPaint = math.ceil(fSquareFeet/fFeetperGallon)
    return iGallonofPaint

#define funtion and pasing two parameter them multiply and get Hours of labor
def getHoursofLabor(fHourperGallon, iGallonofPaint) -> float:
    fHoursofLabor = fHourperGallon * iGallonofPaint
    return fHoursofLabor
#define funtion and pasing two parameter them multiply and get Paint Charge
def getPaintCharge(fPriceperGallon,iGallonofPaint) -> float:
    fPaintCharge = fPriceperGallon * iGallonofPaint
    return fPaintCharge


#define funtion and pasing two parameter them multiply and get Labor Charge
def getLaborCharge(fLaborChargeHours, fHoursofLabor) -> float:
    fLaborCharge = fLaborChargeHours * fHoursofLabor
    return fLaborCharge

#define funtion and pasing two parameter them multiply and get Taxes for input state in line 34
def SaleTax(fPaintandLabor,sSTateTax):
    SaleTax = fPaintandLabor * sSTateTax
    return SaleTax
#define funtion and pasing two parameter them addition and get Paint and Labor charge
def getPaintandLabor(fLaborCharge, fPaintCharge) -> float:
    fPaintandLabor = fLaborCharge + fPaintCharge
    return fPaintandLabor
#define funtion and pasing 4 parameter  for Show to the user  the estimate.and using \n new line.
def getShowCostEstimate(iGallonofPaint,fHoursofLabor,fPaintCharge,fLaborCharge,fTax,fTotalCharge ):
    print(f"Gallon of Paint: {iGallonofPaint}\nHours of labor: {fHoursofLabor:.1f}")
    print(f"Paint Charge: ${fPaintCharge:,.2f}\nLabor Charge: ${fLaborCharge:,.2f}")
    print(f"Tax Charge:   ${fTax:,.2f}\nTotal Charge: ${fTotalCharge:,.2f}")





#define main funtion the program will start on line 80

def main():
    print("!Welcome to paint Job!")
    fSquareFeet = getFloatInput("Enter wall space square feet: ", 0)
    fPriceperGallon = getFloatInput("Enter paint price per gallon: ", 0)
    fFeetperGallon = getFloatInput("Enter feet per gallon: ", 0)
    fHourperGallon = getFloatInput("Enter How many labor hours per gallon: ", 0)
    fLaborChargeHours = getFloatInput("Labor charge per hours: ", 0)
    sState = input("State job is in:").upper()
    sStateTax = getStateTax(sState)
    sLastName = input("Customer Last Name: ")


    #Logic  all the parameter for my funtion calculation
    iGallonofPaint = getGallonofPaint(fSquareFeet, fFeetperGallon)
    fHoursofLabor = getHoursofLabor(fHourperGallon, iGallonofPaint)
    fPaintCharge = getPaintCharge(fPriceperGallon, iGallonofPaint)
    fLaborCharge = getLaborCharge(fLaborChargeHours, fHoursofLabor)
    fPaintandLabor = getPaintandLabor(fLaborCharge, fPaintCharge)
    fTaxes = SaleTax(fPaintandLabor,sStateTax)
    fTotalCharge = fPaintandLabor + fTaxes



    #output for print pass in funtion using 6 parameter from my logic in line 93 to 99
    getShowCostEstimate(iGallonofPaint, fHoursofLabor, fPaintCharge, fLaborCharge, fTaxes, fTotalCharge)

    #Output Save Data into File format text using with open because close automatic no need write close.
    with open(f'{sLastName}_PaintJobOutput.txt', 'w') as OutDataFile:
        OutDataFile.write(f"Name: {sLastName}\nWall space square feet: {fSquareFeet}\n"
                      f"Paint price per gallon: {fPriceperGallon}\nFeet per gallon: {fFeetperGallon}\n"
                      f"Labor hours per gallon: {fHourperGallon}\nLabor charge per hours: {fLaborChargeHours}\n"
                      f"State job is in: {sState}\nGallon of Paint: {iGallonofPaint}\n"
                      f"Hours of labor: {fHoursofLabor:.1f}\nPaint Charge: ${fPaintCharge:,.2f}\n"
                      f"Labor Charge: ${fLaborCharge:,.2f}\nTax Charge: ${fTaxes:,.2f}\n"
                      f"Total cost: ${fTotalCharge:,.2f}")

    print(f"File: {sLastName}_PaintJobOutput.txt was created.")

main()
