# continue statement
i=0
for i in range(12):
    if (i ==8):
     print("Control skipped since the value was 8")    
     continue
    print("6 X",i,"=",6*i)

# break statement
i=0
for i in range(12):
    if (i ==8):
        break
    print("6 X",i,"=",6*i)
print("Control went away since the value was 8")    
