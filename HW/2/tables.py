import time #so the user gets a chance to read the previous line before the next one gets printed

### Introduction ###
print("Hello there, this program allows you (the user) to be able to access all the number times tables going up to 12")
print
time.sleep(1.5)
print("Please be aware that you will have to restart the program each time you want a times table displayed")
print
time.sleep(1.5)

### Main Program ###
timesTable = int(input("Please enter a times table (it can be any number) >>> "))
#gets input from the user (can be any number)
for i in range (1,13):
    print (timesTable, ' X ', i, ' = ',(timesTable * i))#displays chosen times table
    
