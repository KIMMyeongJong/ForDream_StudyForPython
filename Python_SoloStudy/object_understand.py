
class Car :
    color = ""
    brand = ""
    kinds = ""
    def __init__(self,color, brand, kinds):
        self.brand = brand
        self.color = color
        self.kinds = kinds
    def make_car (self):
        print("색상 : " + self.color)
        print("종류 : " + self.kinds)
        print("회사 : " + self.brand)

Car("red","bmw","sports").make_car()
Car("black","venz","truck").make_car()