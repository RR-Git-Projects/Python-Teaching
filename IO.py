#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#  IO.py shows how to do various kinds of input and output operations in python.
#
#  Created by Robert Radloff, 2025-02-22
#  Last edit: 2025-02-22
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

print("This is console output!")

# Read text in from the console and store it to var1.
var1 = input("Type a line of text and press enter: ")
print("You typed: " + var1)

# Read a file from the local directory.
infile = open("text.txt")

# Read the first line of infile.
line1 = infile.readline()
print(line1)

# Close infile.
infile.close()

# Open a new file for writing text to persistent memory.
outfile = open("outfile.txt","w")
outfile.write(line1)
outfile.close()