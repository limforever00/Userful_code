from ProductDAO import *
from ProductVO import Product

class Controller:
    def __init__(self):
        print()

    def select(self):
        ProductDAO().select()

    def searchItem(self):
        choice = input('검색종류 입력 : 상품명/제조회사 : ')
        sendTxt = ''
        if choice == '상품명':
            sendTxt = 'prdName'
        elif choice == '제조회사':
            sendTxt = 'prdMaker'
        else :
            print('잘못된 입력입니다. ')
            return False 
        
        searchTxt = input('검색할 키워드 입력 : ')
        ProductDAO().searchItem(sendTxt, searchTxt)

    def insert(self):
        prdNo = input('상품번호 입력 : ')
        prdName = input('상품명 입력 : ')
        prdPrice = input('가격 입력 : ')
        prdMaker = input('메이커 입력 : ')
        prdColor = input('색상 입력 : ')
        ctgNo = input('카테고리 넘버 입력 : ')
        pro = Product(prdNo, prdName, prdPrice, prdMaker, prdColor, ctgNo)
        ProductDAO().insert(pro)

    def update(self):
        prdNo = input('상품번호 입력 : ')
        prdName = input('상품명 입력 : ')
        prdPrice = input('가격 입력 : ')
        prdMaker = input('메이커 입력 : ')
        prdColor = input('색상 입력 : ')
        ctgNo = input('카테고리 넘버 입력 : ')
        pro = Product(prdNo, prdName, prdPrice, prdMaker, prdColor, ctgNo)
        ProductDAO().update(pro)

    def delete(self):
        bookNo = input('삭제할 도서번호 입력 : ')   
        ProductDAO().delete(bookNo)