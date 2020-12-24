from random import *
import numpy as np
import itertools
import matplotlib.pyplot as plt


r = int(input("좌표평면 r : "))
n = int(input("파티션 개수 n : "))
k = int(input("파티션 당 터미널 개수 k : "))


coordinates = [[] for i in range(k)]

def findBiggerThanPow():
    global n
    cnt = 1
    while (cnt*cnt < n):
        cnt = cnt+1
    return cnt

powFlag = findBiggerThanPow() #제곱근수
terminalPart = [[] for i in range(powFlag*powFlag)] #각 비율에 맞추어 저장한 터미널들 배열

def makeRandomCoorForAxis(randomCoorForAxis):
    global r
    flag = int(r/(powFlag-1))
    subFlag = flag
    subFirst = 1
    randomCoorForAxis.append(0)
    randomCoorForAxis.append(r)
    for i in range (powFlag-1):
        randomCoorForAxis.append(randint(subFirst, flag))
        flag = flag + subFlag
        subFirst = subFirst + subFlag
    randomCoorForAxis.sort()

randomAxisX = []
randomAxisY = []

makeRandomCoorForAxis(randomAxisX)
makeRandomCoorForAxis(randomAxisY)

nPart = [[] for i in range(powFlag)]#dividePart를 통해 좌하단 우상단 저장하기위한 보조 배열
dPart = [[] for i in range(powFlag*powFlag)] #dividePart를 통해 좌하단 우상단 저장하는 배열


num = 0
q = 0
p = 4
cnt = 0

def makeRandomXY():
    global coordinates
    cntX = cntY = 0
    for i in range(powFlag * powFlag):
        for j in range(k):
            helpCoordinates = [[]]
            coorX = round(uniform(randomAxisX[cntX], randomAxisX[cntX+1]), 2)
            helpCoordinates[0].append(coorX)
            coorY = round(uniform(randomAxisY[cntY], randomAxisY[cntY+1]), 2)
            helpCoordinates[0].append(coorY)
            while helpCoordinates in coordinates:
                helpCoordinates = [[]]
                coorX = round(uniform(randomAxisX[cntX], randomAxisX[cntX+1]), 2)
                helpCoordinates[0].append(coorX)
                coorY = round(uniform(randomAxisY[cntY], randomAxisY[cntY+1]), 2)
                helpCoordinates[0].append(coorY)
            coordinates[j]= helpCoordinates
        cntX = cntX+1
        if (cntX == powFlag):
            cntY = cntY+1
            cntX = 0
        coordinates = list(itertools.chain(*coordinates)) #2차원배열로 변형
        # coordinates = list(itertools.chain(*coordinates))
        terminalPart[i] = coordinates
        coordinates = [[] for i in range(k)]


def dividePartition (powFlag): #좌하단 우상단 구하는 함수
    global num, p, q, cnt
    for i in range (powFlag):
        for j in range (powFlag):
            if (i == 0):
                nPart[i].append(randomAxisX[j])
                nPart[i].append(randomAxisY[0])
                nPart[i].append(randomAxisX[j+1])
                nPart[i].append(randomAxisY[1])
            elif (i == 1):
                nPart[i].append(randomAxisX[j])
                nPart[i].append(randomAxisY[1])
                nPart[i].append(randomAxisX[j+1])
                nPart[i].append(randomAxisY[2])
            elif (i == 2):
                nPart[i].append(randomAxisX[j])
                nPart[i].append(randomAxisY[2])
                nPart[i].append(randomAxisX[j+1])
                nPart[i].append(randomAxisY[3])
            elif (i == 3):
                nPart[i].append(randomAxisX[j])
                nPart[i].append(randomAxisY[3])
                nPart[i].append(randomAxisX[j+1])
                nPart[i].append(randomAxisY[4])
            elif (i == 4):
                nPart[i].append(randomAxisX[j])
                nPart[i].append(randomAxisY[4])
                nPart[i].append(randomAxisX[j+1])
                nPart[i].append(randomAxisY[5])
            elif (i == 5):
                nPart[i].append(randomAxisX[j])
                nPart[i].append(randomAxisY[5])
                nPart[i].append(randomAxisX[j+1])
                nPart[i].append(randomAxisY[6])
    for i in range (powFlag*powFlag):
        dPart[i] = nPart[num][q:p]
        q = q+4
        p = p+4
        cnt = cnt+1
        if (cnt == powFlag):
            p = 4
            q = 0
            num = num+1
            cnt = 0

dividePartition (powFlag)

mergeNum = []
def chooseMergePartition (): #병합할 파티션 구하기
    global n, mergeNum
    while len(mergeNum) < (powFlag*powFlag-n):
        num = randint(0, (powFlag*powFlag)-(powFlag+1))
        mergeNum.append(num)
        if num in mergeNum: #중복제거
            mSet = set(mergeNum)
            mergeNum = list(mSet)



chooseMergePartition()

# 좌표값, 좌하단우상단 병합
def doMerge ():
    global terminalPart, dPart
    reversenum = (powFlag*powFlag)-1
    for reversenum in range((powFlag*powFlag)-1, -1, -1):
        while reversenum in mergeNum:
            terminalPart[reversenum] = terminalPart[reversenum] + terminalPart[reversenum+powFlag]
            terminalPart[reversenum+4] = [[]]
            dPart[reversenum].extend(dPart[reversenum+4])
            dPart[reversenum] = dPart[reversenum][0:2] + dPart[reversenum][6:8]
            dPart[reversenum+4] = []
            break
    for i in range (len(terminalPart)):
        if len(terminalPart[i]) > 1:
            mergedPartitionTerminal.append(terminalPart[i])
            mergedPartitiondPart.append(dPart[i])

def makeFourCoor():
    for i in range(len(mergedPartitiondPart)):
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][0])
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][1]) #좌하단
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][3])
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][2]) #우하단
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][0])
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][3]) #좌상단
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][2])
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][3]) #우상단




mergedPartitionTerminal = []
mergedPartitiondPart = []
makeRandomXY()
doMerge()
mergedPartitionFourPart = [[] for i in range(len(mergedPartitiondPart))]

makeFourCoor()










