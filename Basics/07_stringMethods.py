a="Swapnil"
#I cannot change string "a" since string is immutable
print(len(a))
print(a.upper())#will give a new string that is converted to Upper case. Original string remains as it is in smaller case .
print(a.lower())#again a new string will be created.

#Stripping the right hand side characters.
str="!! !! Sw ap ni l! !!"
print(str.rstrip("!"))#will not strip left handside characters.

#Replace
print(str.replace("Swapnil","Ishaan"))

#Splitting a string to a list.
print(str.split(" "))

#Capitalize
blogHeading="intRo tO JS"
print(blogHeading.capitalize())#will convert only the first character of the string to uppercase and rest 
#other characters to lowercase

#centre 
str2="Welcome Home"
print(len(str2))
print(str2.center(40))#will add 12 spaces to make it center aligned.

#count
str3="Welcome to the encyclopedia"
print(len(str3))
print(str3.count("c"))#will count the number of characters.

str4="edmi!!"
print(str4.endswith("!!"))
print(str4.endswith("d",0,5))# This means , is the string ending with "d" or not.

#find()
str5="This is my programming yard"
print(str5.find("is"))#returns the first occurence of the asked string.
#if the string asked is not present then it will return -1.

#index()
# print(str5.index("dfbhfd"))
#will giveb the error and exit since string is not present .

#isalnum()
str6="ksajbkajsdb"
print(str6.isalnum())#returns if the string is alphanumeric or not 

#isalpha()
str6="ksaAASSWWjsdb"
print(str6.isalpha())#returns if the string is alphabetic or not 

#islower()
str7="sdfsf"
print(str7.islower())

str8="asdsdd \n "
print(str8.isprintable()) #since back slash n is not a printable character.

#isspace
print(str8.isspace())#returns true only if the string contains space .

#istitle()
print(str8.istitle())#returns true only if teh first letter of each word if in capitals.

#isupper()
#startswith()
#swapcase()--> swaps the cases of the letters in a string .

#title
str9="This is me the progranmer"
print(str9.title())#will convert the string to title where every starting letter will be in caps.