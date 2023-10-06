from pymongo import MongoClient

class ProductDAO:
    __conn = None;
    __db = None;

    def __init__(self):
        pass

    def connect(self):
        self.__conn = MongoClient(host='localhost', port=27017)
        self.__db = self.__conn.newDB

    def disconect(self):
        self.__conn.close()

    def select(self):
        self.connect()
        res = self.__db.product.find()

        for i in res:
            print(i)
        
        self.disconect()

    def insert(self, product):
        self.connect()
        products = { "prdNo" :product.get_prdNo(),"prdName":product.get_prdName(), "prdPrice":product.get_prdPrice()}
        self.__db.product.insert_one(products)

        self.disconect()

    def update(self, product):
        self.connect()
        self.__db.product.update_one({"prdNo":product.get_prdNo()},{"$set":{"prdName":product.get_prdName(),"prdPrice":product.get_prdPrice()}})
        self.disconect()

    def delete(self, prdNo):
        self.connect()
        self.__db.product.delete_one({"prdNo":prdNo})
        self.disconect()
    
    def searchItem(self, category, txt):
        self.connect()

        res = self.__db.product.find({ category : { "$regex": txt} })

        for i in res:
            print(i)

        self.disconect()