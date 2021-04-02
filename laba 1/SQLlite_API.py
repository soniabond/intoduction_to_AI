import sqlite3


class CosmeticDataRepository:
    def __init__(self, connection):
        self.conn = connection
        self.cursor = connection.cursor()

    def insertRowIntoPartOfFace(self, title):
        self.cursor.execute("""
        insert into part_of_face (title) values (?)
        """, (title,))
        self.conn.commit()

    def insertRowIntoBrand(self, title):
        self.cursor.execute("""
        insert into brand (title) values (?)
        """, (title,))
        self.conn.commit()

    def insertRowIntoCountryProducer(self, title):
        self.cursor.execute("""
        insert into country_producer (title) values (?)
        """, (title,))
        self.conn.commit()

    def insertRowIntoTypeOfCosmetis(self, title):
        self.cursor.execute("""
        insert into type_of_cosmetic (title) values (?)
        """, (title,))
        self.conn.commit()

    def insertRowIntoCosmeticItem(self, title, price, part_of_face_id, country_producer_id, brand_id, type_id):
        self.cursor.execute("""
                insert into cosmetic_items (title, price, part_of_face_id, country_producer_id, brand_id) 
                values (?, ?, ?, ?, ?)
                """, (title, price, part_of_face_id, country_producer_id, brand_id,))
        self.conn.commit()
        self.cursor.execute("select id from cosmetic_items where title=?", (title,))
        row = self.cursor.fetchall()
        row = row[0][0]
        self.cursor.execute("insert into type_item (item_id, type_id) values (?, ?)", (row, type_id))
        self.conn.commit()

    def findPartOfFaceIdByName(self, title):
        self.cursor.execute("select id from part_of_face where title=?", (title,))
        row = self.cursor.fetchall()
        if row == []:
            return -1
        return row[0][0]

    def findBrandIdByName(self, title):
        self.cursor.execute("select id from brand where title=?", (title,))
        row = self.cursor.fetchall()
        if row == []:
            return -1
        return row[0][0]

    def findCountryProducerIdByName(self, title):
        self.cursor.execute("select id from country_producer where title=?", (title,))
        row = self.cursor.fetchall()
        if row == []:
            return -1
        return row[0][0]

    def findTypeOfCosmeticByName(self, title):
        self.cursor.execute("select id from type_of_cosmetic where title=?", (title,))
        row = self.cursor.fetchall()
        if row == []:
            return -1
        return row[0][0]

    def findSpecificCosmeticItems(self, minPrice, maxPrice, partOfFace, countryProducer, brand, type):
        if type == "":
            type_id = "(select type_id from type_item)"
        else:
            type_id = "("+ str(self.findTypeOfCosmeticByName(type)) + ")"
        if brand == "":
            brand_id = "(select id from brand)"
        else:
            brand_id = "("+self.findBrandIdByName(brand).__str__()+")"
        if countryProducer == "":
            countryProducer_id = "(select id from country_producer)"
        else:
            countryProducer_id = "("+self.findCountryProducerIdByName(countryProducer).__str__()+")"
        if partOfFace == "":
            partOfFace_id = "(select id from part_of_face)"
        else:
            partOfFace_id = "("+self.findPartOfFaceIdByName(partOfFace).__str__()+")"
        statement = "select distinct cosmetic_items.title from cosmetic_items, type_item where price between ? and ? and brand_id in " + brand_id.__str__() + " and country_producer_id in " + countryProducer_id.__str__() + " and part_of_face_id in " + partOfFace_id.__str__() + " and type_item.type_id in " + type_id.__str__()
        print(statement)
        self.cursor.execute("select distinct cosmetic_items.title from cosmetic_items, type_item where price between ? and ? and brand_id in " + brand_id.__str__() + " and country_producer_id in " + countryProducer_id.__str__() + " and part_of_face_id in " + partOfFace_id.__str__() + " and type_item.type_id in " + type_id.__str__(), (minPrice, maxPrice,))
        rows = self.cursor.fetchall()
        result = list()
        for i in range(len(rows)):
            result.append(rows[i][0])
        return result
