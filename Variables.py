#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#  Variables.py shows how to define python variables.
#
#  Created by Robert Radloff, 2025-02-22
#  Last edit: 2025-02-22
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

print("test")

# Variable used for testing integer math.
var1=1

print(var1)
print("var1")

var2=3

print(var1+var2)
print(var1/var2)

# Variables used for testing string math.
var3="3"
var4="text"

print(var3)
print(var3+var4)

# Testing string vs int addition.
print(str(var1)+var3)
print(var1+int(var3))

# Testing float conversion.
print(type(var2))
print(type(var1/var2))

var5=var1/var2

print(type(var5))