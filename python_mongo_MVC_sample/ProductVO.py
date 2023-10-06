class Product:
    
    def __init__(self, prdNo, prdName, prdPrice):
        self.__prdNo = prdNo
        self.__prdName = prdName
        self.__prdPrice = prdPrice

    def set_prdNo(self,val):
       self.__prdNo = val

    def set_prdName(self,val):
        self.__prdName = val

    def set_prdPrice(self,val):
        self.__prdPrice = val

    def get_prdNo(self):
        return self.__prdNo
    
    def get_prdName(self):
        return self.__prdName
    
    def get_prdPrice(self):
        return self.__prdPrice
