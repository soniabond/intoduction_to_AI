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




def imageToArray():
    data = np.asarray(Image.open("letters/e31.png"))
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
    values.append(ord('a'))
    imageArrayInit.append(Image.open("letters/a21.png"))
    values.append(ord('a'))
    imageArrayInit.append(Image.open("letters/b11.png"))
    values.append(ord('b'))
    imageArrayInit.append(Image.open("letters/b21.png"))
    values.append(ord('b'))
    imageArrayInit.append(Image.open("letters/c11.png"))
    values.append(ord('c'))
    imageArrayInit.append(Image.open("letters/c21.png"))
    values.append(ord('c'))
    imageArrayInit.append(Image.open("letters/d11.png"))
    values.append(ord('d'))
    imageArrayInit.append(Image.open("letters/d21.png"))
    values.append(ord('d'))
    imageArrayInit.append(Image.open("letters/e11.png"))
    values.append(ord('e'))
    imageArrayInit.append(Image.open("letters/e21.png"))
    values.append(ord('e'))

    # max = np.max(values)
    # min = np.min(values)
    # values = np.array([(x - min) / (max - min) for x in values])
    # valuesResult = []
    # for i in range(len(values)):
    #     valuesResult.append([values[i]])
    #
    # print(valuesResult)
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
    print(np.asarray(valuesResult, dtype=float).T)
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
        print(image_arr.shape)
        imageArrayResult.append(image_arr.copy())



    return np.asarray(imageArrayResult), np.asarray(valuesResult, dtype=float)
