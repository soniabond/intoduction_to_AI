from tkinter import scrolledtext
from tkinter.ttk import Combobox

import SQLlite_API
import table_creation
from tkinter import *

conn = table_creation.createTables()
repository = SQLlite_API.CosmeticDataRepository(conn)

window = Tk()
window.title("cosmetic propositions")
window.geometry("600x600")


lblName = Label(window, text="Name")
lblName.grid(column=0, row=0, pady=5)
lblSelection = Label(window, text="Selection")
lblSelection.grid(column=1, row=0)
lblEmpty = Label(window, text="")
lblEmpty.grid(column=2, row=0, padx=100)

lblMinPrice = Label(window, text="min price")
lblMinPrice.grid(column=0, row=1)
txtMinPrice = Entry(window, width=23, textvariable=50)
txtMinPrice.grid(column=1, row=1)
txtMinPrice.insert(0, 50)

lblMaxPrice = Label(window, text="max price")
lblMaxPrice.grid(column=0, row=2)
txtMaxPrice = Entry(window, width=23, textvariable=2500)
txtMaxPrice.grid(column=1, row=2)
txtMaxPrice.insert(0, 2500)

lblPartOfFace = Label(window, text="part of face")
lblPartOfFace.grid(column=0, row=3)
comboPartOfFace = Combobox(window)
comboPartOfFace['values'] = [""] + table_creation.partOfFaceList
comboPartOfFace.grid(column=1, row=3)

lblCountryProducer = Label(window, text="country producer")
lblCountryProducer.grid(column=0, row=4)
comboCountryProducer = Combobox(window)
comboCountryProducer['values'] = [""] + table_creation.countryList
comboCountryProducer.grid(column=1, row=4)

lblBrand = Label(window, text="brand")
lblBrand.grid(column=0, row=5)
comboBrand = Combobox(window)
comboBrand['values'] = [""] + table_creation.brandList
comboBrand.grid(column=1, row=5)

lblType = Label(window, text="type")
lblType.grid(column=0, row=6)
comboType = Combobox(window)
comboType['values'] = [""] + table_creation.typeList
comboType.grid(column=1, row=6)

infoPanel = scrolledtext.ScrolledText(window, width=60, height=16)
infoPanel.grid(column=0, row=8, columnspan=3, padx=5)


def is_digit(string):
    string = string.replace(',', '.')
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False


def validateVariables(minPrice, maxPrice, partOfFace, countryProducer, brand, typeCosmetic):
    infoPanel.delete(1.0, END)
    if not (is_digit(minPrice) and is_digit(maxPrice)):
        infoPanel.insert(INSERT, "price must be a digit value")
        return False
    if float(minPrice) > float(maxPrice):
        infoPanel.insert(INSERT, "max price must be greater then min price")
        return False
    return True



def generateAnswer():

    minPrice = txtMinPrice.get()
    maxPrice = txtMaxPrice.get()
    partOfFace = comboPartOfFace.get()
    countryProducer = comboCountryProducer.get()
    brand = comboBrand.get()
    typeCosmetic = comboType.get()
    if validateVariables(minPrice, maxPrice, partOfFace, countryProducer, brand, typeCosmetic):
        items = repository.findSpecificCosmeticItems(minPrice, maxPrice, partOfFace, countryProducer, brand,
                                         typeCosmetic)
        infoPanel.insert(INSERT, "Item we can propose\n")
        if items == []:
            infoPanel.insert(INSERT, "no item found")
        else:
            infoPanel.insert(INSERT, items)


btnGetCosmeticItems = Button(window, text="get cosmetic recommendations", command=generateAnswer)
btnGetCosmeticItems.grid(column=0, row=7, columnspan=2, padx=5, pady=10)

window.mainloop()
