class GrandFather:
    grandfather_house = 12

class Father(GrandFather):
    car = "lambo"
    father_house = 5

class Mother:
    jwellery = "gold"
    mother_house = 123

class Son(Father):
    def __init__(self):
        self.house = 123
        self.son_house = super().father_house + self.house

binit = Son()
print(binit.son_house)


# super() le afno direct parent ko property ra method matra access garna sakxa
