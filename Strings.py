#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
#  Strings.py shows how to format and modify strings in python.
#
#  Created by Robert Radloff, 2025-03-03
#  Last edit: 2025-03-03
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#

sentence_1 = "The quick brown fox jumps over a lazy dog"
sentence_2 = "Pack my box with five dozen liquor jugs"

# Print the number of characters in the strings.
#print(len(sentence_1))
#print(len(sentence_2))

# show some multi line printing.
#print("v skipped lines v\n\n\n^ skipped lines ^")
#print("""v skipped lines v


#^ skipped lines ^""")

# Print the first 3 letters of sentence_1 and sentence_2 using a slice.
#print(sentence_1[0:3])
#print(sentence_2[0:3])

# Use the replace function to replace some characters.
#print(sentence_1.replace(" ", "_"))

# Split the sentence into a list of words.
#word_list = sentence_1.split(" ")

# Define a new string to hold our manipulated string.
#reverse_sentence_1 = ""

# Loop through the word list in reverse.
#counter = len(word_list) - 1
#while (counter >= 0):
#    reverse_sentence_1 = reverse_sentence_1 + word_list[counter] + " "
#    counter = counter - 1

#print(reverse_sentence_1)

# Define some floats.
#my_float_1 = 102.0
#my_float_2 = 57.34672
#my_float_3 = 12345.12345

# Define a string with some flags in it to use with the format function.
#printable_string = "my_float_1 = {0}\nmy_float_2 = {1}\nmy_float_3 = {2}"

# Print the floats as a formatted string.
#print(printable_string.format(my_float_1, my_float_2, my_float_3))

# Now lets print everything with 3 fixed decimals.
#printable_string_2 = "\n\":.3f\"\nmy_float_1 = {0:.3f}\nmy_float_2 = {1:.3f}\nmy_float_3 = {2:.3f}"

# Print the floats as a formatted string.
#print(printable_string_2.format(my_float_1, my_float_2, my_float_3))

# Now lets print everything but make them 9 characters long, AND display 3 fixed decimals.
#printable_string_3 = "\n\":9.3f\"\nmy_float_1 = {0:9.3f}\nmy_float_2 = {1:9.3f}\nmy_float_3 = {2:9.3f}"

# Print the floats as a formatted string.
#print(printable_string_3.format(my_float_1, my_float_2, my_float_3))

print("")
print("Done!")