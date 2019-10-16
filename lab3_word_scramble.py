# course: Object-oriented programming, year 2, semester 1
# academic year: 201920
# author: B. Schoen-Phelan
# date: 08-10-2019
# purpose: Lab 3

import string

class WordScramble:
    def __init__(self):
        self.user_input = input("Please give me a sentence: ")

    def scramble(self):
        # print what was input
        print("The user input was: ", self.user_input)

        # first scramble is just one word
        # reverse two indices
        # particularly good to use is to switch the first two
        # and the last two
        # this only makes sense if you have a world that is longer than 3

        if len(self.user_input) > 3:
            #do something
            new_word = self.user_input[0] + self.user_input[2] + self.user_input[1] + self.user_input[3:]
        elif len(self.user_input) <= 3:
            #use_the_original
            new_word = self.user_input
        else:
            print("try again!")
            new_word = False#/0/-1 (Show error)

        print(new_word)



        # now try to scramble one sentence
        # do just words first, then you can move on to work on
        # punctuation
        sentence = self.user_input.strip().split()
        for word in sentence:
            if len(word) > 3:
                #do something
                #need container I can swap stuff in
                #do swap
                temp_word = list(word)
                if (',' in temp_word):
                    #swap but keep position of the comma (,)
                    temp = temp_word[1]
                    temp_word[1] = temp_word[-3]
                    temp_word[-3] = temp
                else:
                    temp = temp_word[1]
                    temp_word[1] = temp_word[2]
                    temp_word[2] = temp

                #put characters together
                temp_word = ''.join(temp_word)
                #put word into the right location
                sentence[index] = temp_word

                swapped_word = ''.join(temp_word)
            else:
                #new word is the same as input
                sentence[index] = word
            #reassemble the word and then the sentence
            #join the words from the list to one sentence for nice print out
            sentence = ''.join(sentence)
            #print the new word
            print(swapped_word)
word_scrambler = WordScramble()
word_scrambler.scramble()

