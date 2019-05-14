""" Pig Latin Practice Project """

def main():
    """
    If start with a vowel character, then add "way" at the end of word;
    If start with a consonant, move the consonant to the end of word, and add "ay" at the end of word as well.
    """

    vowel_chars = ['a','e','i','o','u']

    while True:
        words = input("Please input a word and press enter to finish the input:\n ")

        wordList = words.split(' ')

        for i in range(len(wordList)):
            if wordList[i][0:1].lower() in vowel_chars:
                wordList[i] = wordList[i] + 'way'
            elif not wordList[i]:
                wordList[i] = wordList[0]
            else:
                wordList[i] = ''.join(wordList[i][1:]) + ''.join(wordList[i][0:1]) + 'ay'
        
        newWords = ' '.join(wordList)

        print("The Pig Latin of [{}] is [{}]".format(words,newWords))

        print("\n\n")
        
        exit_key = input("Press any key to continue unless type n ...\n")
        if exit_key.lower() == 'n': 
            break
        

    input("Press any key to exit.")

if __name__ == "__main__":
    main()