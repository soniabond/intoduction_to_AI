from PIL import Image
import numpy as np

#constants
letters = ['A', 'B', 'C', 'D', 'E']


def findIndexOfMaxValue(row):
    max = -100
    index = 0
    for i in range(len(row)):
        if row[i] > max:
            max = row[i]
            index = i
    return index


def defineLetter(row):
    index = findIndexOfMaxValue(row)
    return letters[index]


def imageToArray(path):
    data = np.asarray(Image.open(path))
    image_arr = []
    if (data.ndim == 3):
        for i in range(6):
            for j in range(6):
                image_arr.append(data[i][j][0])
    else:
        for i in range(6):
            for j in range(6):
                image_arr.append(data[i][j])
    max = np.max(image_arr)
    min = np.min(image_arr)
    image_arr = np.array([(x - min) / (max - min) for x in image_arr])
    return image_arr


def initXAndY():
    imageArrayInit = []
    values = []
    imageArrayInit.append(Image.open("letters/a11.png"))

    imageArrayInit.append(Image.open("letters/a21.png"))

    imageArrayInit.append(Image.open("letters/b11.png"))

    imageArrayInit.append(Image.open("letters/b21.png"))

    imageArrayInit.append(Image.open("letters/c11.png"))

    imageArrayInit.append(Image.open("letters/c21.png"))

    imageArrayInit.append(Image.open("letters/d11.png"))

    imageArrayInit.append(Image.open("letters/d21.png"))

    imageArrayInit.append(Image.open("letters/e11.png"))

    imageArrayInit.append(Image.open("letters/e21.png"))



    valuesResult = [['1', '0', '0', '0', '0'],
                    ['1', '0', '0', '0', '0'],
                    ['0', '1', '0', '0', '0'],
                    ['0', '1', '0', '0', '0'],
                    ['0', '0', '1', '0', '0'],
                    ['0', '0', '1', '0', '0'],
                    ['0', '0', '0', '1', '0'],
                    ['0', '0', '0', '1', '0'],
                    ['0', '0', '0', '0', '1'],
                    ['0', '0', '0', '0', '1']
                    ]

    imageArrayResult = []

    for i in range(len(imageArrayInit)):
        data = np.asarray(imageArrayInit[i])
        image_arr = []
        if(data.ndim == 3):
            for i in range(6):
                for j in range(6):
                    image_arr.append(data[i][j][0])
        else:
            for i in range(6):
                for j in range(6):
                    image_arr.append(data[i][j])
        max = np.max(image_arr)
        min = np.min(image_arr)
        image_arr = np.array([(x - min) / (max - min) for x in image_arr])

        imageArrayResult.append(image_arr.copy())



    return np.asarray(imageArrayResult), np.asarray(valuesResult, dtype=float)
