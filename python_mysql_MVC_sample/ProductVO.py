class Product:
    
    def __init__(self, prdNo, prdName, prdPrice, prdMaker, prdColor, ctgNo):
        self.__prdNo = prdNo
        self.__prdName = prdName
        self.__prdPrice = prdPrice
        self.__prdMaker = prdMaker
        self.__prdColor = prdColor
        self.__ctgNo = ctgNo

    def set_prdNo(self,val):
       self.__prdNo = val

    def set_prdName(self,val):
        self.__prdName = val

    def set_prdPrice(self,val):
        self.__prdPrice = val

    def set_prdMaker(self,val):
        self.__prdMaker = val

    def set_prdColor(self,val):
        self.__prdColor = val

    def set_ctgNo(self,val):
        self.__ctgNo = val

    def get_prdNo(self):
        return self.__prdNo
    
    def get_prdName(self):
        return self.__prdName
    
    def get_prdPrice(self):
        return self.__prdPrice
    
    def get_prdMaker(self):
        return self.__prdMaker
    
    def get_prdColor(self):
        return self.__prdColor
    
    def get_ctgNo(self):
        return self.__ctgNo