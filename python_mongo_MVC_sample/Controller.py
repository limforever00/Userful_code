from ProductDAO import *
from ProductVO import Product

class Controller:
    def __init__(self):
        print()

    def select(self):
        ProductDAO().select()

    def insert(self):
        prdNo = input('상품번호 입력 : ')
        prdName = input('상품명 입력 : ')
        prdPrice = input('가격 입력 : ')
        pro = Product(prdNo, prdName, prdPrice)
        ProductDAO().insert(pro)

    def update(self):
        prdNo = input('상품번호 입력 : ')
        prdName = input('상품명 입력 : ')
        prdPrice = input('가격 입력 : ')
        pro = Product(prdNo, prdName, prdPrice)
        ProductDAO().update(pro)

    def delete(self):
        bookNo = input('삭제할 도서번호 입력 : ')   
        ProductDAO().delete(bookNo)

    def searchItem(self):

        sendTxt = 'prdName'

        
        searchTxt = input('검색할 키워드 입력 : ')
        ProductDAO().searchItem(sendTxt, searchTxt)