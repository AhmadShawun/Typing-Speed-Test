from time import *
import random as r

def mistake(parTest,userInputTest): #calculate the typing mistack
    error = 0
    for i in range(len(parTest)):
        try:
            if parTest[i] != userInputTest[i]:
                error = error + 1
        except:
            error = error + 1
    return error





test = ["A paragragraph is a self-contained unit of discourse in write","I am Ahmad Shawun", "welcome the python"] 

test1 = r.choice(test) #randomly show the test set result
print('      ****** typing speed ******** ')
print(test1)
print() # breaking for 1 line
print() # brack for 2 lines

testInput = input(" Enter: ")