#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#  Conditionals.py shows how to use conditional statements and comparison operators in python.
#
#  Created by Robert Radloff, 2025-02-22
#  Last edit: 2025-02-22
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

var1 = 10
var2 = 10

if (var1 == var2):
    print("var1 and var2 are equal!")

if (var1 >= var2):
    print("var1 is greater than OR equal to var2!")

if (var1 > var2 or var1 == var2):
    print("var1 is greater than OR equal to var2!")

if (var1 > var2 and var1 == var2):
    print("This is never true!")
else:
    print("This is always true!")

var3 = input("Enter your own number: ")

try:
    var4 = int(var3)
    if (var1 > var4):
        print("var1 is BIGGER!")
    elif (var1 < var4):
        print("var1 is smaller!")
    else:
        print("var1 is the same as your number!")
        #if(var1 == var4):
            # print("var1 is the same as your number!")
        #else:
            # print("var1 is smaller!")
except:
    print("I told you to enter a number!!! :(")

print("Done!")