import re
import itertools
import collections
import json
from chance import chance

# Functions definition


def readFile():
    with open('sampleText.txt', 'r') as textFile:
        data = textFile.readlines()
    return data


def writeFile(text, stats, uniqueNum, filename="output.json"):
    tempDict = {
        'outputText': text,
        'outputStats': stats,
        'outputUnique': uniqueNum,
    }
    with open(filename, "w+") as outputFile:
        outputFile.write(json.dumps(tempDict))
    print("File successfully written to {}".format(filename))

# This function is for the dfa = starting
# dfa = state (zeroth) of DFA


def start(c):
    if (c == 'o'):
        dfa = 1
    elif (c == 'f'):
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
    elif(c == 'u'):
        dfa = 28
    elif(c == 'i'):
        dfa = 36
    elif(c == 'e'):
        dfa = 42
    elif(c == 'n'):
        dfa = 45
    elif(c == 'w'):
        dfa = 46
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
    elif(c == 'f'):
        dfa = 33
    elif(c == 's'):
        dfa = 35
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
        dfa = 58
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


def state28(c):
    if (c == 'n'):
        dfa = 29
    else:
        dfa = -1
    return dfa


def state29(c):
    if (c == 'l'):
        dfa = 38
    elif(c == 't'):
        dfa = 30
    else:
        dfa = -1
    return dfa


def state30(c):
    if (c == 'i'):
        dfa = 31
    else:
        dfa = -1
    return dfa


def state31(c):
    if (c == 'l'):
        dfa = 32
    else:
        dfa = -1
    return dfa


def state32(c):
    if (c):
        dfa = -1
    return dfa


def state33(c):
    if (c == 't'):
        dfa = 34
    else:
        dfa = -1
    return dfa


def state34(c):
    if (c == 'e'):
        dfa = 1
    else:
        dfa = -1
    return dfa


def state35(c):
    if (c == 'e'):
        dfa = 1
    else:
        dfa = -1
    return dfa


def state36(c):
    if (c == 'f'):
        dfa = 37
    else:
        dfa = -1
    return dfa


def state37(c):
    if (c):
        dfa = -1
    return dfa


def state38(c):
    if (c == 'e'):
        dfa = 39
    else:
        dfa = -1
    return dfa


def state39(c):
    if (c == 's'):
        dfa = 40
    else:
        dfa = -1
    return dfa


def state40(c):
    if (c == 's'):
        dfa = 41
    else:
        dfa = -1
    return dfa


def state41(c):
    if (c):
        dfa = -1
    return dfa


def state42(c):
    if (c == 'i'):
        dfa = 43
    else:
        dfa = -1
    return dfa


def state43(c):
    if (c == 't'):
        dfa = 44
    else:
        dfa = -1
    return dfa


def state44(c):
    if (c == 'h'):
        dfa = 34
    else:
        dfa = -1
    return dfa


def state45(c):
    if (c == 'o'):
        dfa = 1
    elif (c == 'e'):
        dfa = 42
    else:
        dfa = -1
    return dfa


def state46(c):
    if (c == 'h'):
        dfa = 47
    else:
        dfa = -1
    return dfa


def state47(c):
    if (c == 'e'):
        dfa = 48
    elif(c == 'o'):
        dfa = 52
    elif(c == 'i'):
        dfa = 54
    else:
        dfa = -1
    return dfa


def state48(c):
    if (c == 't'):
        dfa = 49
    elif(c == 'r'):
        dfa = 50
    elif(c == 'n'):
        dfa = 52
    else:
        dfa = -1
    return dfa


def state49(c):
    if (c == 'h'):
        dfa = 34
    else:
        dfa = -1
    return dfa


def state50(c):
    if (c == 'e'):
        dfa = 51
    else:
        dfa = -1
    return dfa


def state51(c):
    if (c == 'v'):
        dfa = 34
    elif(c == 'a'):
        dfa = 40
    elif(c):
        dfa = -1
    return dfa


def state52(c):
    if (c == 'm'):
        dfa = 55
    elif(c == 'e'):
        dfa = 53
    elif(c == 's'):
        dfa = 22
    elif(c):
        dfa = -1
    return dfa


def state53(c):
    if (c == 'v'):
        dfa = 34
    else:
        dfa = -1
    return dfa


def state54(c):
    if (c == 'l'):
        dfa = 22
    elif(c == 'c'):
        dfa = 56
    else:
        dfa = -1
    return dfa


def state55(c):
    if (c == 'e'):
        dfa = 53
    elif(c):
        dfa = -1
    return dfa


def state56(c):
    if (c == 'h'):
        dfa = 57
    else:
        dfa = -1
    return dfa


def state57(c):
    if (c == 'e'):
        dfa = 53
    elif(c):
        dfa = -1
    return dfa


def state58(c):
    if(c == 't'):
        dfa = 59
    elif(c == 'n'):
        dfa = 60
    else:
        dfa = -1
    return dfa


def state59(c):
    if(c):
        dfa = -1
    return dfa


def state60(c):
    if(c):
        dfa = -1
    return dfa


def split(string):
    return string.split(" ")


def DFA(data):
    finalOutput = list()
    outputDict = dict()
    # Preprocessing the strings
    for lines in data:
        # split string into list by whitespace
        line = lines.split(" ")
        # retain and separate the newline character from words with whitespace
        # split the separated string into list by whitespace
        line = [split(i[:-1] + " " + i[-1:])
                if re.match(r'([^\s]+)\n', i) else i for i in line]
        flattenedList = []
        # flatten the list if found nested list
        for i in line:
            if isinstance(i, list):
                for item in i:
                    flattenedList.append(item)
            else:
                flattenedList.append(i)

        tempList = list()

        acceptingStates = [2, 6, 9, 12, 18, 23,
                           32, 35, 37, 41, 51, 52, 55, 57, 59, 60]

        for word in flattenedList:
            currentState = 0
            for char in word:
                char = char.casefold()
                if(re.match(r'[~`!@#$%^&()_={}[\]:;,.<>+\/?-]', char)):
                    continue

                # DFA starts here
                if (currentState == 0):
                    currentState = start(char)
                elif (currentState == 1):
                    currentState = state1(char)
                elif (currentState == 2):
                    currentState = state2(char)
                elif (currentState == 3):
                    currentState = state3(char)
                elif (currentState == 4):
                    currentState = state4(char)
                elif (currentState == 5):
                    currentState = state5(char)
                elif (currentState == 6):
                    currentState = state6(char)
                elif (currentState == 7):
                    currentState = state7(char)
                elif (currentState == 8):
                    currentState = state8(char)
                elif (currentState == 9):
                    currentState = state9(char)
                elif (currentState == 10):
                    currentState = state10(char)
                elif (currentState == 11):
                    currentState = state11(char)
                elif (currentState == 12):
                    currentState = state12(char)
                elif (currentState == 13):
                    currentState = state13(char)
                elif (currentState == 14):
                    currentState = state14(char)
                elif (currentState == 15):
                    currentState = state15(char)
                elif (currentState == 16):
                    currentState = state16(char)
                elif (currentState == 17):
                    currentState = state17(char)
                elif (currentState == 18):
                    currentState = state18(char)
                elif (currentState == 19):
                    currentState = state19(char)
                elif (currentState == 20):
                    currentState = state20(char)
                elif (currentState == 21):
                    currentState = state21(char)
                elif (currentState == 22):
                    currentState = state22(char)
                elif (currentState == 23):
                    currentState = state23(char)
                elif (currentState == 24):
                    currentState = state24(char)
                elif (currentState == 25):
                    currentState = state25(char)
                elif (currentState == 26):
                    currentState = state26(char)
                elif (currentState == 27):
                    currentState = state27(char)
                elif (currentState == 28):
                    currentState = state28(char)
                elif (currentState == 29):
                    currentState = state29(char)
                elif (currentState == 30):
                    currentState = state30(char)
                elif (currentState == 31):
                    currentState = state31(char)
                elif (currentState == 32):
                    currentState = state32(char)
                elif (currentState == 33):
                    currentState = state33(char)
                elif (currentState == 34):
                    currentState = state34(char)
                elif (currentState == 35):
                    currentState = state35(char)
                elif (currentState == 36):
                    currentState = state36(char)
                elif (currentState == 37):
                    currentState = state37(char)
                elif (currentState == 38):
                    currentState = state38(char)
                elif (currentState == 39):
                    currentState = state39(char)
                elif (currentState == 40):
                    currentState = state40(char)
                elif (currentState == 41):
                    currentState = state41(char)
                elif (currentState == 42):
                    currentState = state42(char)
                elif (currentState == 43):
                    currentState = state43(char)
                elif (currentState == 44):
                    currentState = state44(char)
                elif (currentState == 45):
                    currentState = state45(char)
                elif (currentState == 46):
                    currentState = state46(char)
                elif (currentState == 47):
                    currentState = state47(char)
                elif (currentState == 48):
                    currentState = state48(char)
                elif (currentState == 49):
                    currentState = state49(char)
                elif (currentState == 50):
                    currentState = state50(char)
                elif (currentState == 51):
                    currentState = state51(char)
                elif (currentState == 52):
                    currentState = state52(char)
                elif (currentState == 53):
                    currentState = state53(char)
                elif (currentState == 54):
                    currentState = state54(char)
                elif (currentState == 55):
                    currentState = state55(char)
                elif (currentState == 56):
                    currentState = state56(char)
                elif (currentState == 57):
                    currentState = state57(char)
                elif (currentState == 58):
                    currentState = state58(char)
                elif (currentState == 59):
                    currentState = state59(char)
                elif (currentState == 60):
                    currentState = state60(char)

            if (currentState in acceptingStates):
                matchedGroup = re.match(
                    r'(|[~`!@#$%^&()_={}[\]:;,.<>+\/?-])(\w+)(|[ ~`!@#$%^&()_={}[\]:;,.<>+\/?-])', word)
                matchedWord = matchedGroup.group(2)
                tempWord = re.sub(r'[^\w]', ' ', word).strip().casefold()
                if (outputDict.get(tempWord) is None):
                    outputDict[tempWord] = 0
                outputDict[tempWord] += 1
                index = word.find(matchedWord)
                word = word[:index] + '<b>' + word[index:index +
                                                   len(matchedWord)] + '</b>' + word[index+len(matchedWord):]
                # alt way
                # if (colorDict.get(word) is None):
                #     colorDict[word] = chance.color()
                # word = "<b style='color:{};'> {} </b>".format(colorDict.get(word), word)
            tempList.append(word)
        tempString = " ".join(tempList)
        finalOutput.append(tempString)
    finalOutput = " ".join(finalOutput)
    return finalOutput, outputDict


# Main code
data = readFile()

finalOutput, outputDict = DFA(data)

writeFile(finalOutput, outputDict, len(outputDict))
