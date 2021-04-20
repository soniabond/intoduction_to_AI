from tkinter import *
from PIL import Image, ImageTk
import ex

pathes = ["letters/a31.png", "letters/b31.png", "letters/c31.png", "letters/d31.png", "letters/e31.png", "letters/a41.png"
          , "letters/b41.png", "letters/c41.png", "letters/d41.png", "letters/e41.png"]
window = Tk()
window.title("letters classification")
window.geometry("1300x800")


lblFunc = Label(window, text="Программа распознает образы букв A, B, C, D, E. Выберете образ с помощью чек бокса")
lblFunc.grid(column=0, row=0, columnspan=3)

infoPanelMaxExtrX = Label(window, text="Оптимальное количество эпох обучения: 5000, 10000")
infoPanelMaxExtrX.grid(column=0, row=1, columnspan=3)

choice = IntVar()

canvasA = Canvas(window, height=200, width=200)
imageA = Image.open("letters/a32.png")
photoA = ImageTk.PhotoImage(imageA)
imageA = canvasA.create_image(0, 0, anchor='nw',image=photoA)
canvasA.grid(row=2,column=0)

choiceA = Radiobutton(text="", value=1, variable=choice, padx=97, pady=0)
choiceA.grid(row=3, column=0, sticky=W)

canvasB = Canvas(window, height=200, width=200)
imageB = Image.open("letters/b32.png")
photoB = ImageTk.PhotoImage(imageB)
imageB = canvasB.create_image(0, 0, anchor='nw',image=photoB)
canvasB.grid(row=2,column=1)

choiceB = Radiobutton(text="", value=2, variable=choice, padx=97, pady=0)
choiceB.grid(row=3, column=1, sticky=W)

canvasC = Canvas(window, height=200, width=200)
imageC = Image.open("letters/c32.png")
photoC = ImageTk.PhotoImage(imageC)
imageC = canvasC.create_image(0, 0, anchor='nw',image=photoC)
canvasC.grid(row=2,column=2)

choiceC = Radiobutton(text="", value=3, variable=choice, padx=97, pady=0)
choiceC.grid(row=3, column=2, sticky=W)

canvasD = Canvas(window, height=200, width=200)
imageD = Image.open("letters/d32.png")
photoD = ImageTk.PhotoImage(imageD)
imageD = canvasD.create_image(0, 0, anchor='nw',image=photoD)
canvasD.grid(row=2,column=3)

choiceD = Radiobutton(text="", value=4, variable=choice, padx=97, pady=0)
choiceD.grid(row=3, column=3, sticky=W)

canvasE = Canvas(window, height=200, width=200)
imageE = Image.open("letters/e32.png")
photoE = ImageTk.PhotoImage(imageE)
imageE = canvasE.create_image(0, 0, anchor='nw',image=photoE)
canvasE.grid(row=2,column=4)

choiceE = Radiobutton(text="", value=5, variable=choice, padx=97, pady=0)
choiceE.grid(row=3, column=4, sticky=W)

canvasA1 = Canvas(window, height=200, width=200)
imageA1 = Image.open("letters/a42.png")
photoA1 = ImageTk.PhotoImage(imageA1)
imageA1 = canvasA1.create_image(0, 0, anchor='nw',image=photoA1)
canvasA1.grid(row=4,column=0)

choiceA1 = Radiobutton(text="", value=6, variable=choice, padx=97, pady=0)
choiceA1.grid(row=5, column=0, sticky=W)

canvasB1 = Canvas(window, height=200, width=200)
imageB1 = Image.open("letters/b42.png")
photoB1 = ImageTk.PhotoImage(imageB1)
imageB1 = canvasB1.create_image(0, 0, anchor='nw',image=photoB1)
canvasB1.grid(row=4,column=1)

choiceB1 = Radiobutton(text="", value=7, variable=choice, padx=97, pady=0)
choiceB1.grid(row=5, column=1, sticky=W)

canvasC1 = Canvas(window, height=200, width=200)
imageC1 = Image.open("letters/c42.png")
photoC1 = ImageTk.PhotoImage(imageC1)
imageC1 = canvasC1.create_image(0, 0, anchor='nw',image=photoC1)
canvasC1.grid(row=4,column=2)

choiceC1 = Radiobutton(text="", value=8, variable=choice, padx=97, pady=0)
choiceC1.grid(row=5, column=2, sticky=W)

canvasD1 = Canvas(window, height=200, width=200)
imageD1 = Image.open("letters/d42.png")
photoD1 = ImageTk.PhotoImage(imageD1)
imageD1 = canvasD1.create_image(0, 0, anchor='nw',image=photoD1)
canvasD1.grid(row=4,column=3)

choiceD1 = Radiobutton(text="", value=9, variable=choice, padx=97, pady=0)
choiceD1.grid(row=5, column=3, sticky=W)

canvasE1 = Canvas(window, height=200, width=200)
imageE1 = Image.open("letters/e42.png")
photoE1 = ImageTk.PhotoImage(imageE1)
imageE1 = canvasE1.create_image(0, 0, anchor='nw',image=photoE1)
canvasE1.grid(row=4,column=4)

choiceE1 = Radiobutton(text="", value=10, variable=choice, padx=97, pady=0)
choiceE1.grid(row=5, column=4, sticky=W)

epochLbl = Label(window, text="количество эпох обучения")
epochLbl.grid(column=0, row=6, pady=20)
epochInfo = Entry(window, width=23, textvariable=10000)
epochInfo.grid(column=1, row=6, pady=20)


def doTrain():
    epoch = epochInfo.get()
    epoch = int(epoch)
    ex.trainModel(epoch)
    infoPanel.delete(1.0, END)
    infoPanel.insert(INSERT, "тренировка окончена")



def doRecognise():
    if choice.get() is None:
        return
    path = pathes[choice.get() - 1]
    letter = ex.makePrediction(path)
    infoPanel.delete(1.0, END)
    infoPanel.insert(INSERT, letter)


btnTrain = Button(window, text="обучить", command=doTrain)
btnTrain.grid(column=0, row=7, columnspan=1, pady=10)

btnDetect = Button(window, text="распознать", command = doRecognise)
btnDetect.grid(column=1, row=7, columnspan=1, pady=10)

infoPanel = Text(window, width=50, height=10)
infoPanel.grid(column=1, row=8, columnspan=1)

ex.trainModel(5000)




window.mainloop()
