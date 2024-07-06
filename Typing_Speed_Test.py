from time import *
import random as r

def mistake(parTest, userInputTest): #calculate the typing mistack
    error = 0
    for i in range(len(parTest)):
        try:
            if parTest[i] != userInputTest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speedTime(timeStart, timeEnd, userInput): # speed time
    # 1) initial time
    # 2) end time
    # 3) word per second (time/word)
    timeDelay = timeEnd - timeStart
    timeRoundOff = round(timeDelay, 2) # 2digit
    speed = len(userInput) / timeRoundOff
    return round(speed) 
if __name__ == '__main__':
    while True:
        ck = input( " Ready to test : yes / no : ")
        if ck == "yes":
            test = ["A paragragraph is a self-contained unit of discourse in write","I am Ahmad Shawun", "welcome to the python"] 

            test1 = r.choice(test) #randomly show the test set result
            print('      ****** typing speed ******** ')
            print(test1)
            print() # breaking for 1 line
            print() # brack for 2 lines

            time1 = time() # fristly take the time when it started
            testInput = input(" Enter: ")
            time2 = time() # end the time when user done

            print(' Speed : ',speedTime(time1, time2, testInput), 'word/second')
            print(' Error : ', mistake(test1, testInput))
        elif ck == "no":
            print(" Thank you for visiting this")
            break
        
        else:
            print(" Wrong input")
