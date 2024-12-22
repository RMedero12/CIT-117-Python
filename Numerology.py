# Author: Ricardo Medero


from numerology1 import Numerology


def main():
    # Get user input for name and birthdate
    while True:
        sName = input("Enter your full name: ")

        Birthday = input("Enter your birth date (mm-dd-yyyy): ")
        if Birthday[2] == "-" or "/" and Birthday[5] == "-" or "/" and len(Birthday) >= 10:
            break
    # Create Numerology object
    numerology = Numerology(sName,  Birthday)

    # Display the results
    print(f"\nNumerology Reading for {numerology.getName()} "
        f"\nBorn on: {numerology.getBirthDate()}"
        f"\nLife Path Number: {numerology.getLifePath()}"
        f"\nBirthday Number: {numerology.getBirthday()}"
        f"\nAttitude Number: {numerology.getAttitude()}"
        f"\nSoul Number: {numerology.getSoul()}"
        f"\nPersonality Number: {numerology.getPersonality()}"
        f"\nPower Name Number: {numerology.getPowerName()}"
        f"\nLife Path Description: {numerology.LifePathDescription}")


main()
