import pymysql

class ProductDAO:
    __conn = None;
    __cursor = None;

    def __init__(self):
        pass

    def connect(self):
        self.__conn = pymysql.connect(host='localhost', db='sqldb3', port=3306,user='root', password='1234', charset='utf8')
        self.__cursor = self.__conn.cursor()

    def disconect(self):
        self.__conn.close()
        self.__cursor.close()

    def select(self):
        self.connect()
        sql = 'select * from product'
        self.__cursor.execute(sql)
        res = self.__cursor.fetchall()
        for i in res:
            print(i)

        self.disconect()
    
    def searchItem(self, category,txt):
        self.connect()
        sql = "select * from product where " + category + " like '%" + txt +"%'"
        self.__cursor.execute(sql)
        res = self.__cursor.fetchall()

        for i in res:
            print(i)

        self.disconect()

    def insert(self, product):
        self.connect()
        val = (product.get_prdNo(), product.get_prdName(), product.get_prdPrice(), product.get_prdMaker(), product.get_prdColor(), product.get_ctgNo())
        sql = 'insert into product values( %s, %s, %s, %s, %s, %s)'
        self.__cursor.execute(sql, val)
        self.__conn.commit()
        self.disconect()

    def update(self, product):
        self.connect()
        val = (product.get_prdName(), product.get_prdPrice(), product.get_prdMaker(), product.get_prdColor(), product.get_ctgNo(), product.get_prdNo())
        sql = 'update product set prdName = %s, prdPrice = %s, prdMaker = %s, prdColor = %s, ctgNo = %s where prdNo = %s'
        self.__cursor.execute(sql, val)
        self.__conn.commit()
        self.disconect()

    def delete(self, prdNo):
        self.connect()
        sql = 'delete from product where prdNo = %s'
        self.__cursor.execute(sql,prdNo)
        self.__conn.commit()
        self.disconect()