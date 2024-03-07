string_words = '''A fish (pl.: fish or fishes) is an aquatic, gill-bearing vertebrate
 animal with swimming fins and a hard skull, but lacking limbs with digits. 
 Fish can be grouped into the more basal jawless fish and the more common jawed fish, the latter including all 
 living cartilaginous and bony fishes,
as well as the extinct placoderms and acanthodians. Most fish are cold-blooded, their body 
temperature varying with the surrounding water, though some large active swimmers like white 
shark and tuna can hold a higher core temperature. Fish can communicate acoustically with each other, 
such as during courtship displays.'''













# Split the string into a list of words.
word_list = string_words.split()

# Create a list of word frequencies using list comprehension.
word_freq = [word_list.count(n) for n in word_list]

# Print the original string, the list of words, and pairs of words along with their frequencies.
print("String:\n {} \n".format(string_words))
print("List:\n {} \n".format(str(word_list)))
print("Pairs (Words and Frequencies:\n {}".format(str(list(zip(word_list, word_freq)))))