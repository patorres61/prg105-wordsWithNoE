# This program will read a text file of words and print out any words do not contain the letter E

# Define variables
noEcount = 0
wordsWithE = 0
totalWords = 0

# Define input file
fin = open('words.txt')

print ('Words Containing No Letter E\n')


# Read file, check character count in each line
def has_no_e(word):
    if 'e' in word:     # check if there is the letter in in the word
        return False    # the letter e has been found in the word, so "has no e" result is false
    else:
        return True     # the letter e is not found in the word, so "has no e" result is true


for line in fin:
    word = line.strip()         # line.strip will strip out any blank spaces
    if word != '    ':
        totalWords += 1         # count total words in file
        has_no_e(word)
        if has_no_e(word) is True:
            noEcount += 1       # count words with no letter e and print out the word
            print word
        else:
            wordsWithE += 1     # count words with the letter e

percent = 100 * (noEcount / float(totalWords))
print ('\nTotal number of words in file with no letter E: ' + str(noEcount))
print ('\nTotal number of words in file containing the letter E: ' + str(wordsWithE))
print ('\nTotal number of words in file: ' + str(totalWords))
print ('\nPercentage of words in file with no letter E is: ' + str(round(percent, 4)) + '%')
