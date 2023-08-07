class Car:
    base_price = 100000 #class variable

    def __init__(self,model,brand):
        self.model = model
        self.brand = brand

    def display_price(self):
        print(f"The base price is {self.base_price}")  

    @classmethod
    def update_base_price(cls,inflation):
        cls.base_price=cls.base_price + (cls.base_price * (inflation/100))

car1=Car("BMW","EV")
car1.display_price()
print(car1.base_price)


Car.update_base_price(10)
print(Car.base_price) 

# =============================================================================================


