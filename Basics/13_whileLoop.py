i=0
while (i<5):
    print(i)
    i=i+1

print("Done with the loop")    
print("================")
i=5
while (i>0):
    print(i)
    i=i-1
#we can also use else with while loop
print("================")
i=5
while (i>0):
    print(i)
    i=i-1
else:
    print("I am inside else block")    
print("================")

#we do not have do-while loop in python but we can emulate it 
# do {
#   loop block statement to be executed;
#   }
# while(condition);

secret_word = "python"
counter = 0

while True:
    word = input("Enter the secret word: ").lower()
    counter = counter + 1
    if word == secret_word:
        break
    if word != secret_word and counter > 7: 
        break