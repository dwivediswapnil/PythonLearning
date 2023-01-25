letter= "Hey My name is {} and i work as {}"
name = "Swapnil"
des="QA"
print(letter.format(name,des))
#--------------------------------------
letter= "Hey My name is {1} and i work as {0}"
name = "Swapnil"
des="QA"
print(letter.format(name,des))
#---------------------------------------
#But this is an obselete approach 
#----------------------------------------
#using f-String
print(f"Hey My name is {des} and i work as {name}")
#------------------------------------------
price=29.09023897
txt=f"The value is {price:.2f}" # value will be rounded to 2 decimal places .
print (txt)
print(f"{3*56}")
print(f"{{2*30}}") #if you wish to print with brackets inside f string.