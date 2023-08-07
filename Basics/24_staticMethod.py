#Static method is a method that belong to class but doesn't have access to 
#class itself(via self) or instances.Static methods are defined using
#@staticmethod decorator and are typically used when method do not require
#instance specific data or clas specific data 

#are used when u have a utility function
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

    @staticmethod
    #Main purpose is to get called first.
    def check_year():
        if year==2024:
            return True
        else:
            return False
        
    @staticmethod
    def display_base_price():
        print(Car.base_price)    

car1=Car("BMW","EV")
car1.display_price()
print(car1.base_price)


Car.update_base_price(10)
print(Car.base_price) 
