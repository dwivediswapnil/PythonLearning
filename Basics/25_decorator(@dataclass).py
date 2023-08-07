from dataclasses import dataclass
@dataclass
class Person:
    first_name:str
    last_name:str
#@dataclass automatically create __init__() behind the scene and initialize    

person = Person("Swapnil","Dwivedi")
print(person.first_name , person.last_name)    