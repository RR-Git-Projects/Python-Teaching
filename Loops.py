#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#  Loops.py shows how to use loops and loop controls in python.
#
#  Created by Robert Radloff, 2025-03-03
#  Last edit: 2025-03-03
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

var1 = 0

while (var1 < 5):
    #print(var1)
    #print(var1)
    var1 = var1 + 1

least_fav = 11

# var1 should be 5.
while (var1 < 20):
#while (1 == 1):
    #if(var1 >= 20):
        #break

    if (var1 == least_fav):
        var1 = var1 + 1
        #continue
        break

    if(var1 % 2 == 1):
        print(var1)

    var1 = var1 + 1

for var2 in range(5):
    for var3 in range(5):
        print(var3)
    print(var2)
    print("")

print("")
print("Done!")