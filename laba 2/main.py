import math
from random import *
from tkinter import *


eps = 0.000001
sign = 0


def func(x):
    return x + math.cos(math.radians(2*x))


def mutation(x0, x1):
    return uniform(x0, x1)


def inversion(x):
    global sign
    global eps
    sign = (sign + 1) % 2
    if sign == 0:
        return x - eps
    return x + eps


def crossover(arrayX, x0, x1):
    k = 99
    for i in range(8):
        for j in range(i+1, 8):
            arrayX[k] = (arrayX[i] + arrayX[j]) / 2
            k -= 1

    for i in range(8):
        arrayX[k] = inversion(arrayX[i])
        k -= 1
        arrayX[k] = inversion(arrayX[i])
        k -= 1

    for i in range(8, k):
        arrayX[i] = mutation(x0, x1)

    return arrayX


def sort(x, y, size, reverse):
    for i in range(size):
        for j in range(size):
            if reverse:
                if math.fabs(y[j]) > math.fabs(y[i]):
                    temp = y[i]
                    y[i] = y[j]
                    y[j] = temp
                    temp = x[i]
                    x[i] = x[j]
                    x[j] = temp
            else:
                if math.fabs(y[j]) < math.fabs(y[i]):
                    temp = y[i]
                    y[i] = y[j]
                    y[j] = temp
                    temp = x[i]
                    x[i] = x[j]
                    x[j] = temp
    return x, y


def genetic(x0, x1, extrKind):
    reverse = True
    if extrKind == "min":
        reverse = False
    populationSize = 40
    population = list()
    f = list()
    count = 0
    for i in range(100):
        population.append(mutation(x0, x1))
        f.append(func(population[i]))

    population, f = sort(population, f, populationSize, reverse)
    initSet = population.copy()
    initSet = population[1: 30]
    fLast = f[0]
    while True:
        count += 1
        population = crossover(population, x0, x1)
        for i in range(populationSize):
            f[i] = func(population[i])
        population, f = sort(population, f, populationSize, reverse)
        if count >= 1000 or math.fabs(fLast - f[0]) < eps:
            break
        fLast = f[0]

    return population[0], initSet


def generateAnswer():
    x, vector = genetic(-2, 1, "max")
    infoPanelMinExtrX.delete(1.0, END)
    infoPanelMinExtrX.insert(INSERT, x)
    y = func(x)
    infoPanelMinExtrY.delete(1.0, END)
    infoPanelMinExtrY.insert(INSERT, y)

    x, vector = genetic(-2, 1, "min")
    infoPanelMaxExtrX.delete(1.0, END)
    infoPanelMaxExtrX.insert(INSERT, x)
    y = func(x)
    infoPanelMaxExtrY.delete(1.0, END)
    infoPanelMaxExtrY.insert(INSERT, y)

    infoPanelXVector.delete(1.0, END)
    infoPanelXVector.insert(INSERT, vector)


window = Tk()
window.title("cosmetic propositions")
window.geometry("500x400")


lblName = Label(window, text="Function")
lblName.grid(column=0, row=0, pady=5)
lblFunc = Label(window, text="y = x + cos(2x)")
lblFunc.grid(column=1, row=0)

lblMaxExtrX = Label(window, text="max extr X")
lblMaxExtrX.grid(column=0, row=1)
infoPanelMaxExtrX = Text(window, width=20, height=1)
infoPanelMaxExtrX.grid(column=1, row=1)

lblMaxExtrY = Label(window, text="max extr Y")
lblMaxExtrY.grid(column=0, row=2)
infoPanelMaxExtrY = Text(window, width=20, height=1)
infoPanelMaxExtrY.grid(column=1, row=2)

lblMinExtrX = Label(window, text="min extr X")
lblMinExtrX.grid(column=0, row=3)
infoPanelMinExtrX = Text(window, width=20, height=1)
infoPanelMinExtrX.grid(column=1, row=3, columnspan=1)

lblMinExtrY = Label(window, text="min extr Y")
lblMinExtrY.grid(column=0, row=4)
infoPanelMinExtrY = Text(window, width=20, height=1)
infoPanelMinExtrY.grid(column=1, row=4, columnspan=1)

initXVector = Label(window, text="init X vector")
initXVector.grid(column=0, row=7)
infoPanelXVector = Text(window, width=50, height=10)
infoPanelXVector.grid(column=1, row=7, columnspan=1)

btnGetResult = Button(window, text="get new result", command=generateAnswer)
btnGetResult.grid(column=0, row=6, columnspan=2, padx=5, pady=10)

window.mainloop()