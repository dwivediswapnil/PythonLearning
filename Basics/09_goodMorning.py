import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestampHrs = int(time.strftime('%H'))
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
if(timestampHrs<12):
    print("Good Morning , Swapnil !")
elif(timestampHrs>12 and timestampHrs<15):
    print("Good Afternoon, Swapnil !")
elif(timestampHrs>15 and timestampHrs<18):
    print("Good Evening, Swapnil !")  
else:
    print("Good Night, Swapnil !")      