# This program will read a text file of words and print out any words do not contain the letter E

# Define variables
noEcount = 0
wordsWithE = 0
totalWords = 0

# Define input file
fin = open('words.txt')

# Read input file
fin.readline()

print ('Words Containing No Letter E\n')

# Read file, check character count in each line
def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True

for line in fin:
    word = line.strip()  # line.strip will strip out any blank spaces
    totalWords += 1
    has_no_e(word)
    if has_no_e(word) is True:
        print word
        noEcount += 1
    else:
        wordsWithE += 1

percent = 100 * (noEcount / float(totalWords))
print noEcount
print wordsWithE
print ('\nTotal number of words in file containing the letter E: ' + str(wordsWithE))
print ('\nTotal number of words in file with no letter E: ' + str(noEcount))
print ('\nTotal number of words in file: ' + str(wordsWithE + noEcount))
print ('\nPercentage of words in file with no letter E is: ' + str(round(percent, 2)) + '%')
