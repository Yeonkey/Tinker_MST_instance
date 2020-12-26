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
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][2])
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][1]) #우하단
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][0])
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][3]) #좌상단
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][2])
        mergedPartitionFourPart[i].append(mergedPartitiondPart[i][3]) #우상단




def findNeighbors():
    for i in range(len(mergedPartitiondPart)): # 0~mergedPartitiondPart = P
        for j in range(len(mergedPartitiondPart)): # P' (인접인지 확인할  대상)
            if (i==j):
                pass
            if ((mergedPartitiondPart[j][0] == mergedPartitiondPart[i][2]) and
                    ((mergedPartitiondPart[j][1] == mergedPartitiondPart[i][1]) or
                     (mergedPartitiondPart[j][3] == mergedPartitiondPart[i][3]))):
                #우측에 인접한 놈들을 찾아냈다
                neighborPart[i].append(j)
                if (((mergedPartitionFourPart[i][7] == mergedPartitionFourPart[j][5]) and # 상단
                     (mergedPartitionFourPart[i][3] < mergedPartitionFourPart[j][1])) or
                        ((mergedPartitionFourPart[i][3] == mergedPartitionFourPart[j][1]) and #하단
                         (mergedPartitionFourPart[i][7] > mergedPartitionFourPart[j][5]))):
                    neighborPart[i].append(mergedPartitionFourPart[i][2])
                    neighborPart[i].append(mergedPartitionFourPart[i][3])
                    neighborPart[i].append(mergedPartitionFourPart[i][6])
                    neighborPart[i].append(mergedPartitionFourPart[i][7])
                else:
                    neighborPart[i].append(mergedPartitionFourPart[j][0])
                    neighborPart[i].append(mergedPartitionFourPart[j][1])
                    neighborPart[i].append(mergedPartitionFourPart[j][4])
                    neighborPart[i].append(mergedPartitionFourPart[j][5])
                    #우측에 인접한 놈들에대한 인접좌표를 찾아냈다.
            elif ((mergedPartitionFourPart[i][2] == mergedPartitionFourPart[j][0]) and
                  (mergedPartitionFourPart[i][7] > mergedPartitionFourPart[j][5]) and #우측 중단
                  (mergedPartitionFourPart[i][3] < mergedPartitionFourPart[j][1])) :
                neighborPart[i].append(j)
                neighborPart[i].append(mergedPartitionFourPart[i][2])
                neighborPart[i].append(mergedPartitionFourPart[i][3])
                neighborPart[i].append(mergedPartitionFourPart[i][6])
                neighborPart[i].append(mergedPartitionFourPart[i][7])
            elif ((mergedPartitionFourPart[i][2] == mergedPartitionFourPart[j][0]) and
                  (mergedPartitionFourPart[i][7] < mergedPartitionFourPart[j][5]) and #우측위로엇갈
                  (mergedPartitionFourPart[i][7] > mergedPartitionFourPart[j][1])):
                neighborPart[i].append(j)
                neighborPart[i].append(mergedPartitionFourPart[i][2])
                neighborPart[i].append(mergedPartitionFourPart[i][3])
                neighborPart[i].append(mergedPartitionFourPart[j][4])
                neighborPart[i].append(mergedPartitionFourPart[j][5])
            elif ((mergedPartitionFourPart[i][2] == mergedPartitionFourPart[j][0]) and
                  (mergedPartitionFourPart[i][3] < mergedPartitionFourPart[j][5]) and #우측아래로엇갈
                  (mergedPartitionFourPart[i][3] > mergedPartitionFourPart[j][1])):
                neighborPart[i].append(j)
                neighborPart[i].append(mergedPartitionFourPart[j][0])
                neighborPart[i].append(mergedPartitionFourPart[j][1])
                neighborPart[i].append(mergedPartitionFourPart[i][6])
                neighborPart[i].append(mergedPartitionFourPart[i][7])
            ############################################################################우
            elif ((mergedPartitiondPart[j][2] == mergedPartitiondPart[i][0]) and
                  ((mergedPartitiondPart[j][1] == mergedPartitiondPart[i][1]) or
                   (mergedPartitiondPart[j][3] == mergedPartitiondPart[i][3]))):
                #좌측에 인접한 놈들을 찾아냈다
                neighborPart[i].append(j)
                if (((mergedPartitionFourPart[i][5] == mergedPartitionFourPart[j][7]) and #상단
                     (mergedPartitionFourPart[i][1] < mergedPartitionFourPart[j][3])) or
                        ((mergedPartitionFourPart[i][1] == mergedPartitionFourPart[j][3]) and #하단
                         (mergedPartitionFourPart[i][5] > mergedPartitionFourPart[j][7]))):
                    neighborPart[i].append(mergedPartitionFourPart[i][0])
                    neighborPart[i].append(mergedPartitionFourPart[i][1])
                    neighborPart[i].append(mergedPartitionFourPart[i][4])
                    neighborPart[i].append(mergedPartitionFourPart[i][5])
                else:
                    neighborPart[i].append(mergedPartitionFourPart[j][2])
                    neighborPart[i].append(mergedPartitionFourPart[j][3])
                    neighborPart[i].append(mergedPartitionFourPart[j][6])
                    neighborPart[i].append(mergedPartitionFourPart[j][7])
            elif ((mergedPartitionFourPart[i][0] == mergedPartitionFourPart[j][2]) and
                  (mergedPartitionFourPart[i][7] < mergedPartitionFourPart[j][5]) and
                  (mergedPartitionFourPart[i][3] > mergedPartitionFourPart[j][1])) : #중단
                neighborPart[i].append(j)
                neighborPart[i].append(mergedPartitionFourPart[i][0])
                neighborPart[i].append(mergedPartitionFourPart[i][1])
                neighborPart[i].append(mergedPartitionFourPart[i][4])
                neighborPart[i].append(mergedPartitionFourPart[i][5])
            elif ((mergedPartitionFourPart[i][0] == mergedPartitionFourPart[j][2]) and
                  (mergedPartitionFourPart[j][7] > mergedPartitionFourPart[i][5]) and
                  (mergedPartitionFourPart[j][3] < mergedPartitionFourPart[i][5])):
                neighborPart[i].append(j)
                neighborPart[i].append(mergedPartitionFourPart[i][0])
                neighborPart[i].append(mergedPartitionFourPart[i][1])
                neighborPart[i].append(mergedPartitionFourPart[j][6])
                neighborPart[i].append(mergedPartitionFourPart[j][7]) #좌측위로엇갈
            elif ((mergedPartitionFourPart[i][0] == mergedPartitionFourPart[j][2]) and
                  (mergedPartitionFourPart[j][7] > mergedPartitionFourPart[i][1]) and
                  (mergedPartitionFourPart[j][3] < mergedPartitionFourPart[i][1])):
                neighborPart[i].append(j)
                neighborPart[i].append(mergedPartitionFourPart[j][2])
                neighborPart[i].append(mergedPartitionFourPart[j][3])
                neighborPart[i].append(mergedPartitionFourPart[i][4])
                neighborPart[i].append(mergedPartitionFourPart[i][5]) #좌측아래로엇갈
            ###########################################################################################좌
            elif ((mergedPartitiondPart[j][1] == mergedPartitiondPart[i][3]) and
                  ((mergedPartitiondPart[j][0] == mergedPartitiondPart[i][0]) or
                   (mergedPartitiondPart[j][2] == mergedPartitiondPart[i][2]))):
                #상측에 인접한 놈들을 찾아냈다
                neighborPart[i].append(j)
                neighborPart[i].append(mergedPartitionFourPart[i][4])
                neighborPart[i].append(mergedPartitionFourPart[i][5])
                neighborPart[i].append(mergedPartitionFourPart[i][6])
                neighborPart[i].append(mergedPartitionFourPart[i][7])

            elif ((mergedPartitiondPart[j][3] == mergedPartitiondPart[i][1]) and
                  ((mergedPartitiondPart[j][0] == mergedPartitiondPart[i][0]) or
                   (mergedPartitiondPart[j][2] == mergedPartitiondPart[i][2]))):
                #하측에 인접한 놈들을 찾아냈다
                neighborPart[i].append(j)
                neighborPart[i].append(mergedPartitionFourPart[i][0])
                neighborPart[i].append(mergedPartitionFourPart[i][1])
                neighborPart[i].append(mergedPartitionFourPart[i][2])
                neighborPart[i].append(mergedPartitionFourPart[i][3])

def addPartitionNum():
    global mergedPartitionTerminal
    subArray = [[] for i in range(len(mergedPartitiondPart))]
    for i in range(len(mergedPartitiondPart)):
        for j in range(len(mergedPartitionTerminal[i])):
            subArray[i].append(i)
    subArray = np.array(subArray)
    mergedPartitionTerminal = np.array(mergedPartitionTerminal)
    for i in range (len(mergedPartitiondPart)):
        mergedPartitionTerminal[i] = np.c_[mergedPartitionTerminal[i], subArray[i]]
    mergedPartitionTerminal = mergedPartitionTerminal.tolist()
    mergedPartitionTerminal = list(itertools.chain(*mergedPartitionTerminal)) #2차원 배열로 변형
    mergedPartitionTerminal = list(itertools.chain(*mergedPartitionTerminal)) #2차원 배열로 변형




mergedPartitionTerminal = []
mergedPartitiondPart = []
makeRandomXY()
doMerge()
mergedPartitionFourPart = [[] for i in range(len(mergedPartitiondPart))]
neighborPart = [[] for i in range(len(mergedPartitiondPart))]
finalPartTerminal = [[] for i in range(len(mergedPartitiondPart))]
makeFourCoor()
findNeighbors()

addPartitionNum()


fw=open("Tinkerd_Mst_Instance.txt", "w")
for i in range (len(neighborPart)):
    fw.write(str(i) + ' ')
    fw.write(str(int(len(neighborPart[i])/5)) + ' ')
    for j in range(len(neighborPart[i])):
        fw.write(str(neighborPart[i][j]) + ' ')
    fw.write(str('\n'))

j = 1
while j <= len(mergedPartitionTerminal):
    fw.write(str(mergedPartitionTerminal[j-1]) + ' ')
    fw.write(str(mergedPartitionTerminal[j]) + ' ')
    fw.write(str(int(mergedPartitionTerminal[j+1])))
    fw.write('\n')
    j += 3

fw.close()









