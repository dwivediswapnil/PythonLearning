# *args= positional arguments
# **kwargs = keyword arguments

def hello(*args,**kwargs):
    print(args)
    print(kwargs) 

lst = list(("Swapnil","Dwivedi")) 
dict_val = {"age":22,"dob":1093} 

hello(*lst,**dict_val) #It should be given like this.
#argument has to be given like this.

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
if __name__=="__main__":
    person1 = Person("Swapnil","Dwivedi")
    person1.display()

#If this code is executed , it will check whether __name__==__main__ is there 
# or not ,if yes, then execution will start from there , otherwise it will execute line by line.    
