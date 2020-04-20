import re
import itertools
import collections
import json
from chance import chance

# Functions definition

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
        state = 1
    elif (c == 'f'):
        state = 3
    elif (c == 'a'):
        state = 4
    elif (c == 'y'):
        state = 7
    elif (c == 'b'):
        state = 10
    elif (c == 's'):
        state = 11
    elif (c == 't'):
        state = 13
    elif(c == 'u'):
        state = 28
    elif(c == 'i'):
        state = 36
    elif(c == 'e'):
        state = 42
    elif(c == 'n'):
        state = 45
    elif(c == 'w'):
        state = 46
    # 61 is used to check for any
    # invalid symbol
    else:
        state = 61
    return state


def state1(c):
    if (c == 'r'):
        state = 2
    else:
        state = 61
    return state


def state2(c):
    if (c):
        state = 61
    return state


def state3(c):
    if(c == 'o'):
        state = 1
    else:
        state = 61
    return state


def state4(c):
    if (c == 'n'):
        state = 5
    elif (c == 'l'):
        state = 19
    elif(c == 'f'):
        state = 33
    elif(c == 's'):
        state = 35
    else:
        state = 61
    return state


def state5(c):
    if (c == 'd'):
        state = 6
    else:
        state = 61
    return state


def state6(c):
    if(c):
        state = 61
    return state


def state7(c):
    if (c == 'e'):
        state = 8
    else:
        state = 61
    return state


def state8(c):
    if (c == 't'):
        state = 9
    else:
        state = 61
    return state


def state9(c):
    if (c):
        state = 61
    return state


def state10(c):
    if (c == 'u'):
        state = 8
    elif (c == 'e'):
        state = 24
    else:
        state = 61
    return state


def state11(c):
    if (c == 'o'):
        state = 12
    elif (c == 'i'):
        state = 20
    else:
        state = 61
    return state


def state12(c):
    if (c):
        state = 61
    return state


def state13(c):
    if (c == 'h'):
        state = 14
    else:
        state = 61
    return state


def state14(c):
    if (c == 'o'):
        state = 15
    elif (c == 'a'):
        state = 58
    else:
        state = 61
    return state


def state15(c):
    if (c == 'u'):
        state = 16
    else:
        state = 61
    return state


def state16(c):
    if (c == 'g'):
        state = 17
    else:
        state = 61
    return state


def state17(c):
    if (c == 'h'):
        state = 18
    else:
        state = 61
    return state


def state18(c):
    if (c):
        state = 61
    return state


def state19(c):
    if (c == 't'):
        state = 13
    else:
        state = 61
    return state


def state20(c):
    if (c == 'n'):
        state = 21
    else:
        state = 61
    return state


def state21(c):
    if (c == 'c'):
        state = 22
    else:
        state = 61
    return state


def state22(c):
    if (c == 'e'):
        state = 23
    else:
        state = 61
    return state


def state23(c):
    if (c):
        state = 61
    return state


def state24(c):
    if (c == 'c'):
        state = 25
    else:
        state = 61
    return state


def state25(c):
    if (c == 'a'):
        state = 26
    else:
        state = 61
    return state


def state26(c):
    if (c == 'u'):
        state = 27
    else:
        state = 61
    return state


def state27(c):
    if (c == 's'):
        state = 22
    else:
        state = 61
    return state


def state28(c):
    if (c == 'n'):
        state = 29
    else:
        state = 61
    return state


def state29(c):
    if (c == 'l'):
        state = 38
    elif(c == 't'):
        state = 30
    else:
        state = 61
    return state


def state30(c):
    if (c == 'i'):
        state = 31
    else:
        state = 61
    return state


def state31(c):
    if (c == 'l'):
        state = 32
    else:
        state = 61
    return state


def state32(c):
    if (c):
        state = 61
    return state


def state33(c):
    if (c == 't'):
        state = 34
    else:
        state = 61
    return state


def state34(c):
    if (c == 'e'):
        state = 1
    else:
        state = 61
    return state


def state35(c):
    if (c):
        state = 61
    return state
    # if (c == 'e'):
    #     state = 1
    # else:
    #     state = 61
    # return state


def state36(c):
    if (c == 'f'):
        state = 37
    else:
        state = 61
    return state


def state37(c):
    if (c):
        state = 61
    return state


def state38(c):
    if (c == 'e'):
        state = 39
    else:
        state = 61
    return state


def state39(c):
    if (c == 's'):
        state = 40
    else:
        state = 61
    return state


def state40(c):
    if (c == 's'):
        state = 41
    else:
        state = 61
    return state


def state41(c):
    if (c):
        state = 61
    return state


def state42(c):
    if (c == 'i'):
        state = 43
    else:
        state = 61
    return state


def state43(c):
    if (c == 't'):
        state = 44
    else:
        state = 61
    return state


def state44(c):
    if (c == 'h'):
        state = 34
    else:
        state = 61
    return state


def state45(c):
    if (c == 'o'):
        state = 1
    elif (c == 'e'):
        state = 42
    else:
        state = 61
    return state


def state46(c):
    if (c == 'h'):
        state = 47
    else:
        state = 61
    return state


def state47(c):
    if (c == 'e'):
        state = 48
    elif(c == 'o'):
        state = 52
    elif(c == 'i'):
        state = 54
    else:
        state = 61
    return state


def state48(c):
    if (c == 't'):
        state = 49
    elif(c == 'r'):
        state = 50
    elif(c == 'n'):
        state = 52
    else:
        state = 61
    return state


def state49(c):
    if (c == 'h'):
        state = 34
    else:
        state = 61
    return state


def state50(c):
    if (c == 'e'):
        state = 51
    else:
        state = 61
    return state


def state51(c):
    if (c == 'v'):
        state = 34
    elif(c == 'a'):
        state = 40
    elif(c):
        state = 61
    return state


def state52(c):
    if (c == 'm'):
        state = 55
    elif(c == 'e'):
        state = 53
    elif(c == 's'):
        state = 22
    elif(c):
        state = 61
    return state


def state53(c):
    if (c == 'v'):
        state = 34
    else:
        state = 61
    return state


def state54(c):
    if (c == 'l'):
        state = 22
    elif(c == 'c'):
        state = 56
    else:
        state = 61
    return state


def state55(c):
    if (c == 'e'):
        state = 53
    elif(c):
        state = 61
    return state


def state56(c):
    if (c == 'h'):
        state = 57
    else:
        state = 61
    return state


def state57(c):
    if (c == 'e'):
        state = 53
    elif(c):
        state = 61
    return state


def state58(c):
    if(c == 't'):
        state = 59
    elif(c == 'n'):
        state = 60
    else:
        state = 61
    return state


def state59(c):
    if(c):
        state = 61
    return state


def state60(c):
    if(c):
        state = 61
    return state


def split(string):
    return string.split(" ")


def DFA(data):
    finalOutput = list()
    outputDict = dict()
    # Preprocessing the strings
    for lines in data:
        # split string into list by whitespace
        line = lines.split(" ")
        # separate the newline character from words with whitespace
        # and
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
                if(re.match(r'[~`!@#$%^&()_={}[\]:;,.<>+\/?-]', char) and (currentState == 0 or currentState in acceptingStates)):
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

            coorConj = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']

            if (currentState in acceptingStates):
                matchedGroup = re.match(
                    r'(|[~`!@#$%^&()_={}[\]:;,.<>+\/?-]+)(\w+)(|[ ~`!@#$%^&()_={}[\]:;,.<>+\/?-]+)', word)
                matchedWord = matchedGroup.group(2)
                tempWord = re.sub(r'[^\w]', ' ', word).strip().casefold()

                stats = {
                    'num': 0,
                    'type': ''
                }

                if (outputDict.get(tempWord) is None):
                    outputDict[tempWord] = stats
                outputDict[tempWord]['num'] += 1
                if(tempWord in coorConj):
                    outputDict[tempWord]['type'] = 'Coordinating Conjunction'
                else:
                    outputDict[tempWord]['type'] = 'Subcoordinating Conjunction'
                index = word.find(matchedWord)
                word = word[:index] + '<b>' + word[index:index +
                                                   len(matchedWord)] + '</b>' + word[index+len(matchedWord):]
            tempList.append(word)
        tempString = " ".join(tempList)
        finalOutput.append(tempString)
    finalOutput = " ".join(finalOutput)
    return finalOutput, outputDict


# Main code
def dfa_api(data):
    splitData = data.split('\n')
    splitData = [data + "\n" for data in splitData]
    finalOutput, outputDict = DFA(splitData)
    writeFile(finalOutput, outputDict, len(outputDict))
    return True