# class2.py
class Product:
    def __init__(self, id, name, price):
        self.id = 100
        self.name = "아이폰"
        self.price = 950000
    def print(self) :
        print("{0}, {1}, {2}".format(
            self.id, self.name, self.price
        ))
#인스턴스 생성
p1 = Product(100, "아이폰14", 950000) 
p1.print()       