import re
import itertools
import collections
import json
from chance import chance

def readFile():
    with open('sampleText.txt', 'r') as textFile:
        data = textFile.readlines()
    return data


def writeFile(text, stats, uniqueNum, filename="output.json"):
    tempDict = {
        'outputText' : text,
        'outputStats' : stats,
        'outputUnique' : uniqueNum,
    }
    with open(filename, "w+") as outputFile:
            outputFile.write(json.dumps(tempDict))
    print("File successfully written to {}".format(filename))

# This function is for the dfa = starting
# dfa = state (zeroth) of DFA
def start(c):
    if (c == 'o'):
        dfa = 1
    elif (c == 'n' or c == 'f'):
        dfa = 3
    elif (c == 'a'):
        dfa = 4
    elif (c == 'y'):
        dfa = 7
    elif (c == 'b'):
        dfa = 10
    elif (c == 's'):
        dfa = 11
    elif (c == 't'):
        dfa = 13
    # -1 is used to check for any
    # invalid symbol
    else:
        dfa = -1
    return dfa

def state1(c):
    if (c == 'r'):
        dfa = 2
    else:
        dfa = -1
    return dfa

def state2(c):
    if (c):
        dfa = -1
    return dfa

def state3(c):
    if(c == 'o'):
        dfa = 1
    else:
        dfa = -1
    return dfa

def state4(c):
    if (c == 'n'):
        dfa = 5
    elif (c == 'l'):
        dfa = 19
    else:
        dfa = -1
    return dfa

def state5(c):
    if (c == 'd'):
        dfa = 6
    else:
        dfa = -1
    return dfa

def state6(c):
    if(c):
        dfa = -1
    return dfa

def state7(c):
    if (c == 'e'):
        dfa = 8
    else:
        dfa = -1
    return dfa

def state8(c):
    if (c == 't'):
        dfa = 9
    else:
        dfa = -1
    return dfa

def state9(c):
    if (c):
        dfa = -1
    return dfa

def state10(c):
    if (c == 'u'):
        dfa = 8
    elif (c == 'e'):
        dfa = 24
    else:
        dfa = -1
    return dfa

def state11(c):
    if (c == 'o'):
        dfa = 12
    elif (c == 'i'):
        dfa = 20
    else:
        dfa = -1
    return dfa

def state12(c):
    if (c):
        dfa = -1
    return dfa

def state13(c):
    if (c == 'h'):
        dfa = 14
    else:
        dfa = -1
    return dfa

def state14(c):
    if (c == 'o'):
        dfa = 15
    elif (c == 'a'):
        dfa = 8
    else:
        dfa = -1
    return dfa

def state15(c):
    if (c == 'u'):
        dfa = 16
    else:
        dfa = -1
    return dfa

def state16(c):
    if (c == 'g'):
        dfa = 17
    else:
        dfa = -1
    return dfa

def state17(c):
    if (c == 'h'):
        dfa = 18
    else:
        dfa = -1
    return dfa

def state18(c):
    if (c):
        dfa = -1
    return dfa

def state19(c):
    if (c == 't'):
        dfa = 13
    else:
        dfa = -1
    return dfa

def state20(c):
    if (c == 'n'):
        dfa = 21
    else:
        dfa = -1
    return dfa

def state21(c):
    if (c == 'c'):
        dfa = 22
    else:
        dfa = -1
    return dfa

def state22(c):
    if (c == 'e'):
        dfa = 23
    else:
        dfa = -1
    return dfa

def state23(c):
    if (c):
        dfa = -1
    return dfa

def state24(c):
    if (c == 'c'):
        dfa = 25
    else:
        dfa = -1
    return dfa

def state25(c):
    if (c == 'a'):
        dfa = 26
    else:
        dfa = -1
    return dfa

def state26(c):
    if (c == 'u'):
        dfa = 27
    else:
        dfa = -1
    return dfa

def state27(c):
    if (c == 's'):
        dfa = 22
    else:
        dfa = -1
    return dfa

data = readFile()

# print(data)

finalOutput = list()

def split(string):
    return string.split(" ")

outputDict = dict()
colorDict = dict()
for lines in data:
    # split string into list by whitespace
    line = lines.split(" ")
    # retain and separate the newline character from words with whitespace
    # split the separated string into list by whitespace
    line = [ split(i[:-1] + " " + i[-1:]) if re.match(r'([^\s]+)\n', i) else i for i in line]
    flattenedList = []
    # flatten the list if found nested list
    for i in line:
        if isinstance(i, list):
            # print(i)
            for item in i:
                flattenedList.append(item)
        else:
            flattenedList.append(i)
    # print(flattenedList)
    tempList = list()
    for word in flattenedList:
        dfa = 0
        for char in word:
            char = char.casefold()
            if(char == '.' or char == ','):
                continue

            # dfa starts here
            if (dfa == 0):
                dfa = start(char)
            elif (dfa == 1):
                dfa = state1(char)
            elif (dfa == 2):
                dfa = state2(char)
            elif (dfa == 3):
                dfa = state3(char)
            elif (dfa == 4):
                dfa = state4(char)
            elif (dfa == 5):
                dfa = state5(char)
            elif (dfa == 6):
                dfa = state6(char)
            elif (dfa == 7):
                dfa = state7(char)
            elif (dfa == 8):
                dfa = state8(char)
            elif (dfa == 9):
                dfa = state9(char)
            elif (dfa == 10):
                dfa = state10(char)
            elif (dfa == 11):
                dfa = state11(char)
            elif (dfa == 12):
                dfa = state12(char)
            elif (dfa == 13):
                dfa = state13(char)
            elif (dfa == 14):
                dfa = state14(char)
            elif (dfa == 15):
                dfa = state15(char)
            elif (dfa == 16):
                dfa = state16(char)
            elif (dfa == 17):
                dfa = state17(char)
            elif (dfa == 18):
                dfa = state18(char)
            elif (dfa == 19):
                dfa = state19(char)
            elif (dfa == 20):
                dfa = state20(char)
            elif (dfa == 21):
                dfa = state21(char)
            elif (dfa == 22):
                dfa = state22(char)
            elif (dfa == 23):
                dfa = state23(char)
            elif (dfa == 24):
                dfa = state24(char)
            elif (dfa == 25):
                dfa = state25(char)
            elif (dfa == 26):
                dfa = state26(char)
            elif (dfa == 27):
                dfa = state27(char)
            

        if (dfa == 2 or dfa == 6 or dfa == 9 or dfa == 12 or dfa == 18 or dfa == 23):
            tempWord = re.sub(r'[^\w]', ' ', word).strip().casefold()
            if (outputDict.get(tempWord) is None):
                outputDict[tempWord] = 0
            outputDict[tempWord] += 1
            word = "<b> {} </b>".format(word)
            # alt way
            # if (colorDict.get(word) is None):
            #     colorDict[word] = chance.color()
            # word = "<b style='color:{};'> {} </b>".format(colorDict.get(word), word)
        tempList.append(word)
    tempString = " ".join(tempList)
    finalOutput.append(tempString)
finalOutput = " ".join(finalOutput)

# print(finalOutput)
# print(outputDict)


writeFile(finalOutput, outputDict, len(outputDict))