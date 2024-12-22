#Author: Ricardo Medero

class Numerology:
    def __init__(self, sName, sDOB):
        self.sName = sName
        self.sDOB = sDOB

        # Private method to convert a letter to corresponding number
    def _LettertoNumber(self, letter):
        letter = letter.upper()
        Character_Convertion = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
            'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
            'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
        }
        return Character_Convertion.get(letter, 0)  # If the character is not a letter, return 0
    # Helper method to reduce a number to a single digit
    def _reduceNumber(self, inumber):
        while inumber > 9:
            inumber = sum(int(digit) for digit in str(inumber))
        return inumber

    # Get Name
    @property
    def getName(self):
        return self.sName

    # Get Birth Date
    @property
    def getBirthDate(self):
        return self.sDOB

    # Calculate Life Path Number
    def getLifePath(self):
        # Extract all digits from the date of birth (mm-dd-yyyy)
        iTotal = sum([int(digit) for digit in self.sDOB if digit.isdigit()])

        return self._reduceNumber(iTotal)

    # Calculate Birthday Number
    def getBirthday(self):
        # Extract the day from the birthdate and sum  digits
        day = int(self.sDOB.split('-')[1])  # Assuming format mm-dd-yyyy
        return self._reduceNumber(sum(int(digit) for digit in str(day)))

    # Calculate Attitude Number
    def getAttitude(self):
        # Sum the birth month and the birth day
        iMonth, iDay, _ = self.sDOB.split('-')
        iMonth, iDay = int(iMonth), int(iDay)
        return self._reduceNumber(iMonth + iDay)

    # Calculate Soul Number
    def getSoul(self):
        sLetters = 'AEIOU'
        sName = self.sName.upper()
        iTotal = sum(self._LettertoNumber(char) for char in sName if char in sLetters)
        return self._reduceNumber(iTotal)

    # Calculate Personality Number
    def getPersonality(self):
        sLetters = 'AEIOU'
        sName = self.sName.upper()
        iTotal = sum(self._LettertoNumber(char) for char in sName if char not in sLetters)
        return self._reduceNumber(iTotal)

    # Calculate Power Name Number
    def getPowerName(self):
        # Power Name Number is the sum of Soul Number and Personality Number
        iSoulnumber = self.getSoul()
        iPersonalityNumber = self.getPersonality()
        return self._reduceNumber(iSoulnumber + iPersonalityNumber)


    def LifePathDescription(self):
        # This method returns a string based on the life path number
        life_path = self.getLifePath()
        descriptions = {
            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art, and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often an extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoys nature and water, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"
        }
        return self.LifePathDescription()



