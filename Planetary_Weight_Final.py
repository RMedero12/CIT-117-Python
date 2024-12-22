#Create by Riacrdo Medero
#Date: 10-14-2024
#Planetary Weight with finction and dictionary picking file:
import pickle
#using function for load the history in dictionary if dict is empty will print file not found,
#using error handling for make sure user type alpha character if user type Y
# using for loop to loop in the dictionary and print the History
def loadHistory():
    dictPlanetHistory = {}
    try:
        with open("rmPlanetaryWeights.db", "rb") as file:
            dictPlanetHistory = pickle.load(file)
        while True:
            LoadHistory = input("Would you like to see the history? Y/N: ").upper()
            if not LoadHistory.isalpha():
                print("Must be characters Y or N: ")
                continue
            if LoadHistory == "Y":
                for name, dictWeights in dictPlanetHistory.items():
                    print(f"{name}, here are your weights")
                    for planet, weight in dictWeights.items():
                        print(f"{planet:10s} {weight:10,.2f}")
                break
            if LoadHistory == "N": break
            else:
                print("Must be characters Y or N: ")
    except:
        print("No file found")
    return dictPlanetHistory

#function for get the user weight whit error handling and returned to main for logic
def UserWeigthInput(sPrompt):
    fNumber = 0
    while fNumber <= 0:
        try:
            fNumber = float(input(sPrompt))
        except ValueError:
            print("Input must a numeric value")
    return fNumber

#main fuction were decide wich funtion use first and were evrything return.
# using dictionary for surface name as a key,and weight as a value
def main():
    dictHistory = loadHistory()

    dictSurface = {'MERCURY': 0.38,
                   'VENUS': 0.91,
                   'MOON': 0.165,
                   'MARS': 0.38,
                   'JUPITER': 2.34,
                   'SATURN': 0.93,
                   'URANUS': 0.92,
                   'NEPTUNE': 1.12,
                   'PLUTO': 0.066}
#using while loop for error handling and verify name dont exists in history dictionary
    while True:
        sName = input("Enter Name: ").title()
        if sName in dictHistory:
            print(f"{sName} already exists")
            continue
        if sName == "": break
        #getting the user weight after return from the def UserWeigthInput and using for loop,
        # for loop in dictSurface and getting the value and multiply by User weight
        fWeight = UserWeigthInput("Enter Weight: ")
        dictPersonWeights = {}
        print(f"{sName}, here are your weights on our Solar System's planets")
        for key, value in dictSurface.items():
            fCalculatedWeight = fWeight * value
            dictPersonWeights[key] = fCalculatedWeight
            print(f"{key:10}{fCalculatedWeight:10.2f}")
        dictHistory[sName] = dictPersonWeights
        #using with open to open file for dump the history
        with open("rmPlanetaryWeights.db", "wb") as file:
            pickle.dump(dictHistory, file)
        # using loop for ask if user want to continue with error handling
        while True:
            Continue = input("Do you want to continue? Y/N: ").upper()
            if not Continue.isalpha():
                print("Must be characters Y or N: ")
                continue
            if Continue == "Y":
                break
            if Continue == "N":
                raise SystemExit()
            else:
                print("Must be characters Y or N: ")



main()

