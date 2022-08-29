class Car():
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
        self.wheels_count = 4
        self.top_speed = 100
    
    def honk(self):
        print("HONK")

a_red_car = Car("red", "VW")
print(a_red_car.color)
a_red_car.honk()
