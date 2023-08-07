from dataclasses import dataclass
@dataclass
class Person:
    first_name:str
    last_name:str
#@dataclass automatically create __init__() behind the scene and initialize    

    def age_of_person(self,age,standard):
        print(f'{standard} is {age} years of age.')

person = Person("Swapnil","Dwivedi")
print(person.first_name , person.last_name)    

person.age_of_person(23,"3rd")

