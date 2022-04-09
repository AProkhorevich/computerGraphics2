import math


def getMove(dx: float = 0, dy: float = 0):
    return [[1, 0, dx], [0, 1, dy], [0, 0, 1]]


def getChangeSize(x: float = 0):
    return [[x, 0, 0], [0, x, 0], [0, 0, 1]]


def getReflectionOX():
    return [[1, 0, 0], [0, -1, 0], [0, 0, 1]]


def getReflectionOY():
    return [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]


def getReflectionXY():
    return [[0, 1, 0], [1, 0, 0], [0, 0, 1]]


def getRotation(angle: float):
    return [[math.cos(angle), -math.sin(angle), 0],
            [math.sin(angle), math.cos(angle), 0], [0, 0, 1]]


def setOrigin(origin):
    return [[1, 0, origin[0]], [0, 1, origin[1]], [0, 0, 1]]


def unsetOrigin(origin):
    return [[1, 0, -origin[0]], [0, 1, -origin[1]], [0, 0, 1]]


def reflectionOY(point):
    tMatrix = getReflectionOY()
    pointAsMatrix = mapToMatrixRows(point)
    res = matrixmult(tMatrix, pointAsMatrix)
    return roundUpCoordinates(res)


def rotateAround(point, origin, angle):
    angle = angle * math.pi / 180
    pointAsMatrix = mapToMatrixRows(point)
    res = matrixmult(setOrigin(origin), getRotation(angle))
    res = matrixmult(res, unsetOrigin(origin))
    res = matrixmult(res, pointAsMatrix)
    return roundUpCoordinates(res)


def moveFigure(point, x=0, y=0):
    moveMatrix = getMove(dx=x, dy=y)
    pointAsMatrix = mapToMatrixRows(point)
    res = matrixmult(moveMatrix, pointAsMatrix)
    return roundUpCoordinates(res)


def reflectionOX(point):
    tMatrix = getReflectionOX()
    pointAsMatrix = mapToMatrixRows(point)
    res = matrixmult(tMatrix, pointAsMatrix)
    return roundUpCoordinates(res)


def reflectionOY(point):
    tMatrix = getReflectionOY()
    pointAsMatrix = mapToMatrixRows(point)
    res = matrixmult(tMatrix, pointAsMatrix)
    return roundUpCoordinates(res)


def reflectionXY(point):
    tMatrix = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]
    pointAsMatrix = mapToMatrixRows(point)
    res = matrixmult(tMatrix, pointAsMatrix)
    return roundUpCoordinates(res)


def changeSize(point, origin,  x=1):
    res = matrixmult(setOrigin(origin), getChangeSize(x))
    res = matrixmult(res, unsetOrigin(origin))
    pointAsMatrix = mapToMatrixRows(point)
    res = matrixmult(res, pointAsMatrix)
    return roundUpCoordinates(res)


def mapToMatrixRows(m1):
    return list(map(lambda el: [el], m1))


def matrixmult(left, right):
    sum = 0
    tmp = []
    result = []
    leftRowNumber = len(left)
    leftColumnNumber = len(left[0])
    rightRowNumber = len(right)
    rightColumnNumber = len(right[0])
    if rightRowNumber != leftColumnNumber:
        print("Матрицы не могут быть перемножены")
    else:
        for z in range(0, leftRowNumber):
            for j in range(0, rightColumnNumber):
                for i in range(0, leftColumnNumber):
                    sum += left[z][i] * right[i][j]
                tmp.append(sum)
                sum = 0
            result.append(tmp)
            tmp = []
    return result


def roundUpCoordinates(m1):
    return [round(i[0], 5) for i in m1]
