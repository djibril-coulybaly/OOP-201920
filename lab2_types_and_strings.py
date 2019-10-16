#Course: Object-Oriented Programming, Year 2, Semester 1
#Academic Year: 2019/20
#Author: Djibril Coulybaly
#date: 29-09-2019
#Purpose: Lab 2

class Types_and_Strings:
    def __init__(self):
        pass

    def play_with_strings(self):
        # working with strings
        message = input("Enter your noun: ")
        print("Originally entered: "+ message)

        # print only first and last of the sentence
        print("\nFirst letter: "+message[0])
        print("Last letter: "+message[-1])

        # use slice notation
        print("\nUsing Slice Notation")
        print("--------------------")
        print("First 3 letters: " + message[:3])
        print("Last 3 letters: " + message[-3:])
        print("2nd index onwards: " + message[1:])
        print("Displaying up to the 5th index: " + message[:5])

        # escaping a character
        print("\nPrinting a sentence with quotation marks/apostrophes")
        print("----------------------------------------------------")
        print("\"That\'s fantastic\"!")

        # find all a's in the input word and count how many there are
        print("\nPosition of 1st occurrence of the letter \'a\'")
        firstpos = message.find(str('a'))
        print(firstpos)

        print("\nNumber of occurences of the letter \'a\'")
        print(message.count(str('a')))

        # replace all occurences of the character a with the - sign
        # try this first by assignment of a location in a string and
        # observe what happens, then use replace()

        # This cannot be done as strings are one of the data types
        # that are immutable or cannot change
        # message[firstpos] = '-'
        # print(message)

        print("\nReplace all occurrences of the character \'a\' with the \'-\' sign")
        print(message.replace('a','-'))


        # printing only characters at even index positions
        print("\nPrinting only characters at even index positions")
        print("--------------------------------------------------")
        for i in range(0, len(message), 2):
            print("index[{}] = {}".format(i, message[i]))

    def play_with_lists(self):
        message = input("\nPlease enter a whole sentence: ")
        print("Originally entered: "+ message)

        # hand the input string to a list and print it out
        message_sentence = []
        message_sentence = (message.split())
        print(message_sentence)

        # append a new element to the list and print (Is it on the assumption of 1 word or a whole sentence)
        user_message = input("\nEnter a new element to the list: ")
        message_sentence.append(user_message)
        print(message_sentence)

        # remove from the list in 3 ways
        print("\nUsing function del()")
        del message_sentence[2:6]
        print(message_sentence)

        print("\nUsing function pop()")
        message_sentence.pop(4)
        print(message_sentence)

        print("\nUsing function remove()")
        message_sentence.remove("I")
        print(message_sentence)

        # check if the word cake is in your input list
        word_check = "cake"
        for item in message_sentence:
            if (item == word_check):
                print("\nWord is in List")

        # reverse the items in the list and print
        print("\nPrinting the strings in the list in reverse using the reverse function")
        message_sentence.reverse()
        print(message_sentence)

        # reverse the list with the slicing trick
        print("\nPrinting the strings in the list in reverse using slice notation")
        print(message_sentence[::-1])

        # print the list 3 times by using multiplication
        print("\nPrinting the list 3 times using multiplication")
        print(message_sentence * 3)


tas = Types_and_Strings()
tas.play_with_strings()
tas.play_with_lists()