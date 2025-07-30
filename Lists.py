#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#  Lists.py shows some of the basic kinds of lists, and how to work with them.
#
#  Created by Robert Radloff, 2025-03-03
#  Last edit: 2025-03-03
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

var1 = (1, 5, 10, 20, 50)
print(var1[1])

var2 = [1, 5, 10, 20, 50]
print(var2[1])

var2[1] = 6
print(var2[1])

var2.append(100)
print(var2[5])

var3 = {"alpha" : 1, "bravo" : 5, "charlie" : 10}
print(var3["bravo"])

var4 = {1, 5, 10, 20, 50}

print("")
print("Done!")