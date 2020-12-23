from random import *
import numpy as np
import itertools
import matplotlib.pyplot as plt

r = int(input("좌표평면 r : "))
n = int(input("파티션 개수 n(제곱근) : "))
k = int(input("파티션 당 터미널 개수 k : "))
flag = r / n  # 파티션 간격
vector = np.array([n, n])  # 좌표계 변형 벡터
coordinates = [[] for i in range(k)]
nPart = [[] for i in range(n)]  # dividePart를 통해 좌하단 우상단 저장하기위한 보조 배열
dPart = [[] for i in range(n * n)]  # dividePart를 통해 좌하단 우상단 저장하는 배열
terminalPart = [[] for i in range(n * n)]  # 각 비율에 맞추어 저장한 터미널들 배열

neighborPart = [[] for i in range(n * n)]

finalPart = [[] for i in range(n * n)]

num = 0
q = 0
p = 4
cnt = 0


def randomXY():
    for i in range(k):
        helpCoordinates = [[]]
        CoorX = round(uniform(0, r), 2)
        helpCoordinates[0].append(CoorX)
        CoorY = round(uniform(0, r), 2)
        helpCoordinates[0].append(CoorY)
        while helpCoordinates in coordinates:
            helpCoordinates = [[]]
            CoorX = round(uniform(0, r), 2)
            helpCoordinates[0].append(CoorX)
            CoorY = round(uniform(0, r), 2)
            helpCoordinates[0].append(CoorY)
        coordinates[i] = helpCoordinates


def dividePart(r, n):  # 일단 n = 4일때로 생각함, dPart = 좌하단 우상단
    global num, p, q, cnt
    for i in range(n):  # y축
        subXadd = 0
        for j in range(n):  # x축
            if (i == 0):
                subYadd = i * flag
                nPart[i].append(subXadd)
                nPart[i].append(subYadd)
                subXadd = subXadd + flag
                nPart[i].append(subXadd)
                subYadd = subYadd + flag
                nPart[i].append(subYadd)
            elif (i == 1):
                subYadd = i * flag
                nPart[i].append(subXadd)
                nPart[i].append(subYadd)
                subXadd = subXadd + flag
                nPart[i].append(subXadd)
                subYadd = subYadd + flag
                nPart[i].append(subYadd)
            elif (i == 2):
                subYadd = i * flag
                nPart[i].append(subXadd)
                nPart[i].append(subYadd)
                subXadd = subXadd + flag
                nPart[i].append(subXadd)
                subYadd = subYadd + flag
                nPart[i].append(subYadd)
            elif (i == 3):
                subYadd = i * flag
                nPart[i].append(subXadd)
                nPart[i].append(subYadd)
                subXadd = subXadd + flag
                nPart[i].append(subXadd)
                subYadd = subYadd + flag
                nPart[i].append(subYadd)
            elif (i == 4):
                subYadd = i * flag
                nPart[i].append(subXadd)
                nPart[i].append(subYadd)
                subXadd = subXadd + flag
                nPart[i].append(subXadd)
                subYadd = subYadd + flag
                nPart[i].append(subYadd)
            elif (i == 5):
                subYadd = i * flag
                nPart[i].append(subXadd)
                nPart[i].append(subYadd)
                subXadd = subXadd + flag
                nPart[i].append(subXadd)
                subYadd = subYadd + flag
                nPart[i].append(subYadd)

    for i in range(n * n):
        dPart[i] = nPart[num][q:p]
        q = q + 4
        p = p + 4
        cnt = cnt + 1
        if (cnt == n):
            p = 4
            q = 0
            num = num + 1
            cnt = 0


def changeRatio():
    global coordinates
    subXadd = 0
    subYadd = 0
    cntt = 0
    i = 0
    for i in range(n * n):
        coordinates = [[] for i in range(k)]
        randomXY()
        coordinates = list(itertools.chain(*coordinates))  # 2차원배열로 변형
        coordinates = np.array(coordinates)  # ndarray로 변형
        coordinates = coordinates / vector
        coordinates = coordinates + np.array([subXadd, subYadd])
        coordinates = np.round(coordinates, 2)
        coordinates = np.insert(coordinates, 2, values=i, axis=1)
        coordinates = coordinates.tolist()
        terminalPart[i] = coordinates
        subXadd = subXadd + flag
        cntt = cntt + 1
        if (cntt == n):
            subXadd = 0
            subYadd = subYadd + flag
            cntt = 0


def findNeighbors():
    w = x = y = z = 1
    for i in range(n * n):
        if (i == 0):  # 좌하단
            neighborPart[0] = [i + 1, i + n]
        elif (i == n - 1):  # 우하단
            neighborPart[n - 1] = [n - 1 - 1, n - 1 + n]
        elif (i == (n * n) - n):  # 좌상단
            neighborPart[(n * n) - n] = [(n * n) - n - n, (n * n) - n + 1]
        elif (i == (n * n) - 1):  # 우상단
            neighborPart[(n * n) - 1] = [(n * n) - 1 - n, (n * n) - 1 - 1]
        ###################2 예외#########################
        elif (i % n == 0):  # 맨 좌측
            neighborPart[x * n] = [(x * n) - n, (x * n) + 1, (x * n) + n]
            x += 1
        elif (i % n == n - 1):  # 맨 우측
            neighborPart[(w * n) + (n - 1)] = [(w * n) - 1, (w * n) + (n - 2), (w * n) + n + (n - 1)]
            w += 1
        elif (0 <= i < n):  # 맨 하단
            neighborPart[0 + y] = [0 + y - 1, 0 + y + 1, 0 + y + n]
            y += 1
        elif ((n * n) - n <= i < n * n):  # 맨 상단
            neighborPart[((n * n) - n) + z] = [((n * n) - n) + z - n, ((n * n) - n) + z - 1, ((n * n) - n) + z + 1]
            z += 1
        ###################3 예외#########################
        else:
            neighborPart[i] = [i - n, i - 1, i + 1, i + n]


def neighborCoor():
    for i in range(len(neighborPart)):
        for j in range(len(neighborPart[i])):
            finalPart[i].append(neighborPart[i][j])
            if (i < neighborPart[i][j]):
                finalPart[i].append(dPart[neighborPart[i][j]][0])
                finalPart[i].append(dPart[neighborPart[i][j]][1])  # 인접의 좌하단
                finalPart[i].append(dPart[i][2])
                finalPart[i].append(dPart[i][3])  # 자신의 우상단

            elif (i > neighborPart[i][j]):
                finalPart[i].append(dPart[i][0])
                finalPart[i].append(dPart[i][1])  # 자신의 좌하단
                finalPart[i].append(dPart[neighborPart[i][j]][2])
                finalPart[i].append(dPart[neighborPart[i][j]][3])  # 인접의 우상단


dividePart(r, n)  # 파티션 나누기 및 좌하단 우상단 넣기
# dPart
changeRatio()  # 각 파티션에 비율에 맞게 터미널 넣기
# TerminalPart
findNeighbors()  # 이웃파티션 찾기
# NeighborPart
neighborCoor()
# FinalPart
terminalPart = list(itertools.chain(*terminalPart))  # 2차원 배열로 변경
terminalPart = list(itertools.chain(*terminalPart))  # 1차원 배열로 변경
fw = open("inputfile.txt", "w")
for i in range(len(neighborPart)):
    fw.write(str(i) + ' ')
    fw.write(str(len(neighborPart[i])) + ' ')
    for j in range(len(finalPart[i])):
        fw.write(str(finalPart[i][j]) + ' ')
    fw.write(str('\n'))

j = 1
while j <= len(terminalPart):
    fw.write(str(terminalPart[j - 1]) + ' ')
    fw.write(str(terminalPart[j]) + ' ')
    fw.write(str(terminalPart[j + 1]))
    fw.write('\n')
    j += 3

fw.close()
