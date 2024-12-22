#Paint Jobs with functions
#Author: Ricardo Medero
#update:03/18/24
import math
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
                print("Entry must be greater than or equal to", float(fMinAllowedValue), ", Please try again.")
            else:
                return nUserInput


def getGallonofPaint(fSquareFeet, fFeetperGallon) -> float:
    iGallonofPaint = math.ceil(fSquareFeet/fFeetperGallon)
    return iGallonofPaint


def getHoursofLabor(fHourperGallon, iGallonofPaint) -> float:
    fHoursofLabor = fHourperGallon * iGallonofPaint
    return fHoursofLabor

def getPaintCharge(fPriceperGallon,iGallonofPaint) -> float:
    fPaintCharge = fPriceperGallon * iGallonofPaint
    return fPaintCharge



def getLaborCharge(fLaborChargeHours, fHoursofLabor) -> float:
    fLaborCharge = fLaborChargeHours * fHoursofLabor
    return fLaborCharge

def getPaintandLabor(fLaborCharge, fPaintCharge) -> float:
    fPaintandLabor = fLaborCharge + fPaintCharge
    return fPaintandLabor

def getShowCostEstimate(iGallonofPaint,fHoursofLabor,fPaintCharge,fLaborCharge,fTax,fTotalCharge ) -> float:
    print(f"Gallon of Paint: {iGallonofPaint}\nHours of labor: {fHoursofLabor:.1f}")
    print(f"Paint Charge: ${fPaintCharge:,.2f}\nLabor Charge: ${fLaborCharge:,.2f}")
    print(f"Taxes Charge: ${fTax:,.2f}\nTotal Charge: ${fTotalCharge:,.2f}")


def getSalesTax(sStateTax) -> float:

    match sStateTax:
        case "CT" | "VT":
            fTax = .06
        case "MA":
            fTax = .0625
        case "ME":
            fTax = .0625
        case "RI":
            fTax = .07
        case "VT":
            fTax = .06
        case _:
            fTax = .0
    return fTax


def main():
    print("!Welcome to paint Job!")
    fSquareFeet = getFloatInput("Enter wall space square feet: ", 0)
    fPriceperGallon = getFloatInput("Enter paint price per gallon: ", 0)
    fFeetperGallon = getFloatInput("Enter feet per gallon: ", 0)
    fHourperGallon = getFloatInput("Enter How many labor hours per gallon: ", 0)
    fLaborChargeHours = getFloatInput("Labor charge per hours: ", 0)
    sState = input("State job is in:").upper()
    sStateTax = getSalesTax(sState)
    sLastName = input("Customer Last Name: ")


    #Logic
    iGallonofPaint = getGallonofPaint(fSquareFeet, fFeetperGallon)
    fHoursofLabor = getHoursofLabor(fHourperGallon, iGallonofPaint)
    fPaintCharge = getPaintCharge(fPriceperGallon, iGallonofPaint)
    fLaborCharge = getLaborCharge(fLaborChargeHours, fHoursofLabor)
    fPaintandLabor = getPaintandLabor(fLaborCharge, fPaintCharge)
    fTax = fPaintandLabor * sStateTax
    fTotalCharge = fPaintandLabor + fTax

    # output
    getShowCostEstimate(iGallonofPaint, fHoursofLabor, fPaintCharge, fLaborCharge, fTax, fTotalCharge)

    #Output Save Data into File format text
    OutDataFile = open(f'{sLastName}_PaintJobOutput.txt', 'w')
    OutDataFile.write(f"Name: {sLastName}\nWall space square feet: {fSquareFeet}\n"
                      f"Paint price per gallon: {fPriceperGallon}\nFeet per gallon: {fFeetperGallon}\n"
                      f"Labor hours per gallon: {fHourperGallon}\nLabor charge per hours: {fLaborChargeHours}\n"
                      f"State job is in: {sState}\nGallon of Paint: {iGallonofPaint}\n"
                      f"Hours of labor: {fHoursofLabor:.1f}\nPaint Charge: ${fPaintCharge:,.2f}\n"
                      f"Labor Charge: ${fLaborCharge:,.2f}\nTaxes Charge: ${fTax:,.2f}\n"
                      f"Total cost: ${fTotalCharge:,.2f}")
    OutDataFile.close()
    print(f"File: {sLastName}_PaintJobOutput.txt was created.")

main()
