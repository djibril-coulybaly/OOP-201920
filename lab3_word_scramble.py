# Course: Object-Oriented Programming, Year 2, Semester 1
# Academic Year: 2019/2020
# Author: Djibril Coulybaly
# Date: 08-10-2019
# Purpose: Lab 3

import string
import sys

class WordScramble:
    #Function to ask the user to enter a sentence, alongside some error checking
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")
        if self.user_input.isdigit():
            sys.exit("We would have needed a word not a number")

    #Main Function to carry out the scrambling of the sentence
    def scramble(self):
        # Displaying what the user entered
        print("The user input was: ", self.user_input)

        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3

        # If the length of the word that the user entered is greater than 3,
        # it'll flip the 2nd and 3rd letter around. If the length of the word
        # is less than or equal to 3, it won't scramble the word. Otherwise
        # it'll display an error message
        # if len(self.user_input) > 3:
        #     new_word = self.user_input[0] + self.user_input[2] + self.user_input[1] + self.user_input[3:]
        # elif len(self.user_input) <= 3:
        #     new_word = self.user_input
        # else: # here we assume this word is just one character long or the space character
        #     print("try again")
        #     new_word = False #/0/-1 (Show error)
        #
        # #Display the new scrambled word to the user
        # print(new_word)


        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation
        sentence = self.user_input.strip().split()

        for index, word in enumerate(sentence):
            # If the length of the word entered is greater than 3
            if len(word) > 3:
                temp_word = list(word) # we use a list for item assignment, but could also just use another new string variable
                if (',' in temp_word) or ('.' in temp_word):
                    #swap but keep position of the comma (,)
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-3]
                    temp_word[-3] = temp
                else:
                    # Split the word into a list of characters and swap
                    # This swap leaves first and last the same
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-2]
                    temp_word[-2] = temp

                #put characters together
                swapped_word = ''.join(temp_word)
                #put word into the right location
                sentence[index] = swapped_word
            else:
                # Since the length of the word is less than 3,
                # don't swap the word. The new word will be the same as input
                sentence[index] = word

        #reassemble the word and then the sentence
        #join the words from the list to one sentence for nice print out
        swap = ' '.join(sentence)
        #print the new word
        print(swap)

word_scrambler = WordScramble()
word_scrambler.scramble()
# print(string.punctuation)
