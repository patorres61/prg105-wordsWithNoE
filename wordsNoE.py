# This program will read a text file of words and print out any words that have over 20 characters not including white space

# Define variables
NoEcount = 1
wordsWithE = 0

# Define input file
fin = open('words.txt')

# Read input file
fin.readline()

print ('Words Greater Than 20 characters Omitting Blank Spaces\n')
# Read file, check character count in each line
for line in fin:
    word = line.strip()     # line.strip will strip out any blank spaces
    if 'e' in word:
        wordsWithE += 1
    else:
        print word
        NoEcount += 1

print ('\nTotal number of words in file: ' + str(wordsWithE+NoEcount))
print ('\nTotal number of words in file containing the letter E: ' + str(wordsWithE))
print ('\nTotal number of words in file with no letter E: ' + str(NoEcount))
