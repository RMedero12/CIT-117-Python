#RealStateAnalyzer
#Author:Ricardo Medero
#Create:03/23/24



def getFloatInput(sPrompt: str, fMinAllowedValue = 0 ) -> float:

    while True:
        try:
            nUserInput = float(input(sPrompt))
            if nUserInput <= 0:
                print("Must be greater than 0")
                continue
            return nUserInput
            
        except ValueError:
                print("Must be valid 'Value' ")



def getMedian(Med,my_list) -> float:
    if Med % 2 == 0:
        Media1 = my_list[Med//2]
        Media2 = my_list[Med // 2 - 1]
        Median = (Media1 + Media2)/2
        return Median
    else:
        Median = my_list[Med//2]
        return Median


def main():
    COMMISSION = .03
    ContinuosLoop = 0
    my_list = []

    #i have a while loop for value validation if user input wrong data will be continue on the loop
    #i am using appemd to entry all the ProperValue data into a list.

    while ContinuosLoop != -1:

        fPropertValue = getFloatInput("Enter property sale value: ")
        my_list.append(fPropertValue)
        #I have a second while loop for if the user not input Y or N keep on that loop
        while ContinuosLoop != 1:
            sAnotherValue = input("Enter another value Y or N: ").upper()
            if sAnotherValue == "Y":
                break
            elif sAnotherValue == "N":
                ContinuosLoop = -1
                break
            else:
                print("Must be Y or N")


    my_list.sort()
    iCount = 1
    for i in my_list:
        print(f"Property {iCount} ${i:,.2f}")
        iCount += 1


    Minimum = my_list[0]
    my_list.sort(reverse=True)
    Maximum = my_list[0]
    ListTotal = sum(my_list)
    Average = ListTotal/(iCount - 1)
    Med = len(my_list)
    Median = getMedian(Med, my_list)
    CommissionPayout = ListTotal * COMMISSION


    #Display Output
    print(f"{'Minimum:':15} ${Minimum:,.2f}")
    print(f"{'Maximum:':15} ${Maximum:,.2f}")
    print(f"{'Total:':13}   ${ListTotal:,.2f}")
    print(f"{'Averange:':15} ${Average:,.2f}")
    print(f"{'Media:':12}    ${Median:,.2f}")
    print(f"{'Commission:':16} ${CommissionPayout:,.2f}")











main()
