import math
from tkinter import Button
import matplotlib.pyplot as plt
from numpy import void
from matplotlib.widgets import Button

from matrix import *

# Координаты первого лепестка фигуры
X = [0, math.sqrt(3), 0, -math.sqrt(3), 0]
Y = [0, 3, 8, 3, 0]
Z = [1, 1, 1, 1, 1]

buttons = []


def boardUpdate():
    canvasSide = 80
    ax.clear()
    ax.grid()
    ax.axis('equal')
    ax.set(xlim=(-canvasSide//2, canvasSide//2),
           ylim=(-canvasSide//2, canvasSide//2))


def drawFigure(event=None) -> void:
    boardUpdate()
    fCenter = (X[0], Y[0], Z[0])
    ax.plot(X, Y, c="blue")
    for _ in range(5):
        for i, point in enumerate(zip(X, Y, Z)):
            X[i], Y[i], Z[i] = rotateAround(point, fCenter, 60)

        ax.plot(X, Y, c="blue")


def translateFigure(tFunc: callable, tArgs: list = None):
    if tArgs is None:
        tArgs = []
    for i, point in enumerate(zip(X, Y, Z)):
        X[i], Y[i], Z[i] = tFunc(point, *tArgs)
    drawFigure()


def callChangeSize(event) -> void:
    coef = float(input("Введите коэффициент "))
    translateFigure(changeSize, [(X[0], Y[0], Z[0]), coef])
    return


def callMove(event) -> void:
    dx, dy = [float(x) for x in input("Введите значения dx dy ").split()]
    translateFigure(moveFigure, [dx, dy])
    return


def callReflection(event) -> void:
    availableAxis = {
        'ox': reflectionOX,
        'oy': reflectionOY,
        'xy': reflectionXY,

    }
    while True:
        choice = input("Введите название оси ")
        if choice.lower() in availableAxis:
            translateFigure(availableAxis[choice.lower()])
            return


def callRotateAround(event) -> void:
    angle = float(input("Введите угол вращения"))
    choice = input(
        "Введите точку центра вращения или оставьте пустой для вращения вокруг начала координат").split()
    if len(choice) == 2:
        origin = (float(choice[0]), float(choice[1]))
        translateFigure(rotateAround, [origin, angle])
    else:
        translateFigure(rotateAround, [(0, 0), angle])


def resetFigPos(event=None) -> void:
    '''Задает координатам первого лепестка фигуры значения по умолчанию'''
    global X, Y, Z
    X = [0, math.sqrt(3), 0, -math.sqrt(3), 0]
    Y = [0, 3, 8, 3, 0]
    Z = [1, 1, 1, 1, 1]

    drawFigure()


def setUp(event=None):
    plt.cla
    global ax
    ax = plt.subplot()
    ax.clear()

#  Кнопки
    axes = plt.axes([0.2, 0.000001, 0.1, 0.075])
    moveButton = Button(axes, 'Move')
    moveButton.on_clicked(callMove)
    buttons.append(moveButton)

    axes = plt.axes([0.35, 0.000001, 0.1, 0.075])
    changeSizeButton = Button(axes, 'Change size')
    changeSizeButton.on_clicked(callChangeSize)
    buttons.append(changeSizeButton)

    axes = plt.axes([0.5, 0.000001, 0.1, 0.075])
    resetButton = Button(axes, 'Reset')
    resetButton.on_clicked(resetFigPos)
    buttons.append(resetButton)

    axes = plt.axes([0.7, 0.000001, 0.1, 0.075])
    mirrorButton = Button(axes, 'Miror')
    mirrorButton.on_clicked(callReflection)
    buttons.append(mirrorButton)

    axes = plt.axes([0.9, 0.000001, 0.1, 0.075])
    rotateButton = Button(axes, 'Rotate')
    rotateButton.on_clicked(callRotateAround)
    buttons.append(rotateButton)

    resetFigPos()


if __name__ == '__main__':
    setUp()

    # X, Y, Z = translateFigure(X, Y, Z, moveFigure, [10, 5])
    # drawFigure(X, Y, Z, color="red")

    # translateFigure(moveFigure, [10, 5])
    # drawFigure()

    # X, Y, Z = translateFigure(X, Y, Z, moveFigure, [5])
    # X, Y, Z = translateFigure(X, Y, Z, reflectionOX)

    # X, Y, Z = translateFigure(X, Y, Z, reflectionOY)
    # drawFigure(X, Y, Z, color="green")

    # translateFigure(changeSize, [0.5])
    # drawFigure()

    # translateFigure(rotate_around, [(0, 0), 15])
    # translateFigure(changeSize, [2])
    # drawFigure()

    plt.show()
