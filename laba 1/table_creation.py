import sqlite3
import random
import SQLlite_API

countryList = ["France","USA"]
partOfFaceList = ["Eye", "Lips", "face skin"]
brandList = ["Chanel", "NYX"]
typeList = [ "anti age", "hydration", "sun protection"]
cosmeticItemsList = ["Hydrao'quinn", "Pointyrober Collinotter", "Adazoga", "Hayesphasia", "Washingheart", "Harinabla", "Sanderlotus Bellgrin",
                     "Halda Jaden", "Mavaca", "Frankenlley", "Masonania", "Grubbycollin", "Webbbroom Grangwalker", "Stelama", "Smical",
                     "Reyesfang Evilson", "Capricollins", "Surbrown", "Floresslight", "O'brienfoot",  "Baroshark", "Azrence",
                     "Daviempa", "Myerolga", "Daviseus", "Woon Moraleng Harrism", "Reigan Le Reye"]


def createTables():
    conn = sqlite3.connect("cosmetic_data_table")
    cursor = conn.cursor()

    cursor.execute("drop table if exists part_of_face")
    cursor.execute("drop table if exists brand")
    cursor.execute("drop table if exists country_producer")
    cursor.execute("drop table if exists type_of_cosmetic")
    cursor.execute("drop table if exists type_item")
    cursor.execute("drop table if exists cosmetic_items")
    cursor.execute("""CREATE TABLE IF NOT EXISTS part_of_face (
                       id integer not null primary key autoincrement, 
                       title varchar(256) not null  
                       )
                      
                   """)
    cursor.execute("""create table if not exists country_producer(
                        id integer not null primary key autoincrement, 
                        title varchar(256) not null 
                        )""")
    cursor.execute("""create table if not exists brand(
                        id integer not null primary key autoincrement, 
                        title varchar(256) not null 
                        )""")
    cursor.execute("""create table if not exists type_of_cosmetic(
                        id integer not null primary key autoincrement, 
                        title varchar(256) not null 
                        )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS cosmetic_items (
                       id integer not null primary key autoincrement,
                       title varchar(256) not null ,
                       price integer default 0,
                       part_of_face_id integer ,
                       country_producer_id integer ,
                       brand_id integer ,
                       foreign key (part_of_face_id) references part_of_face(id) ,
                       foreign key (country_producer_id) references country_producer(id) ,
                       foreign key (brand_id) references brand(id)
                       )
                   """)
    cursor.execute("""create table if not exists type_item(
                    item_id integer , 
                    type_id integer , 
                    foreign key (item_id) references cosmetic_items(id) ,
                    foreign key (type_id) references type_of_cosmetic(id)
                    )""")

    countryListLen = len(countryList)
    partOfFaceListLen = len(partOfFaceList)
    brandListLen = len(brandList)
    typeListLen = len(typeList)
    cosmeticItemsListLen = len(cosmeticItemsList)
    maxPrice = 2500
    minPrice = 50

    repository = SQLlite_API.CosmeticDataRepository(conn)

    for i in range(countryListLen):
        repository.insertRowIntoCountryProducer(countryList[i])
    for i in range(partOfFaceListLen):
        repository.insertRowIntoPartOfFace(partOfFaceList[i])
    for i in range(brandListLen):
        repository.insertRowIntoBrand(brandList[i])
    for i in range(typeListLen):
        repository.insertRowIntoTypeOfCosmetis(typeList[i])
    for i in range(cosmeticItemsListLen):
        repository.insertRowIntoCosmeticItem(cosmeticItemsList[i], random.randint(minPrice, maxPrice),
                                             random.randint(1, partOfFaceListLen), random.randint(1, countryListLen),
                                             random.randint(1, brandListLen), random.randint(1, typeListLen))


    return conn
