from Controller import *

class main:
    def __init__(self):
        pass
    
    def start(self):
        control = Controller()
#         상품관리 프로그램
#         기능
#         상품 정보 조회
#         상품 등록 
#         상품 정보 수정
#         상품 삭제
#         검색 
#         검색 종류 / 키워드 입력 받아서 검색 결과 출력 
#         검색 종류
#         상품명 검색
#         제조회사 검색
#         키워드 : 검색어 (값)

        while True:
            num = input('1. 상품 정보 조회 2. 상품 등록 3. 상품 정보 수정 4.상품 정보 삭제 5.상품명 검색 6.종료')

            if num == '1':
                control.select()
                print()
            elif num =='2':
                control.insert()
                print()
            elif num == '3':                
                control.update()
                print()
            elif num == '4':
                control.delete()
                print()
            elif num == '5':
                control.searchItem()
                print()
            elif num == '6':
                break
            else:
                print('잘못 입력했습니다.')


if __name__ == '__main__':
    app = main()
    app.start()
