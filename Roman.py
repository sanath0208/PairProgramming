def strval(self, x: str):  #Function to Parse Each Digit
        if(x=="I"):
            return 1
        elif(x=="V"):
            return 5
        elif(x=="X"):
            return 10
        elif(x=="L"):
            return 50
        elif(x=="C"):
            return 100
        elif(x=="D"):
            return 500
        elif(x=="M"):
            return 1000
        
         
def romanToInt(self, s: str) -> int: #Function to Convert Roman to Integers. Written by Sai Sanath
    prev = 1001                        #Initializing the Prev Variable
    fin = 0
    for i in s:                     #Iterating Each digit
        val = self.strval(i)        #Calling the Util fucntion to parse each digit
        if val>prev:
            fin = fin - 2*prev + val
        else:
            fin = fin + val
        prev = val
    return fin

def intToRoman(self, num: int) -> str:  # method created for changing Integers to Roman Numbers
    sym = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",  # All possible set of roman numbers is assigned to respective integers
        90: "XC",  # Function writtern by Bhagya Rishiroop Boda
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M"

    }

    values = sym.keys()
    result = []

    for val in reversed(values):
        quo, num = divmod(num, val)
        if quo > 0:
            temp = [sym[val]] * quo
            result.extend(temp)

    return ''.join(result)  # gives the resulting roman number