class House:
    window = 10
    door = 3
    color = "Red"

    def __init__(self):
        print("I was called first")
    
    def ghar(self):
        print("Mero ghar ko color", self.color)
    
    def set_color(self, color):
        self.color = color

ram_house = House()
shyam_house = House()
hari_house = House()

print(ram_house.color)
shyam_house.color = "Green"
shyam_house.set_color("Blue")
print(shyam_house.color)
shyam_house.ghar()
ram_house.ghar()
hari_house.ghar()