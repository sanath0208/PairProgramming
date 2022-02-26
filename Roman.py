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