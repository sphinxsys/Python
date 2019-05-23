""" Find palindromes in dictionary file """

import load_dictionary
word_list = load_dictionary.loadfile('2of4brif.txt')
pali_word = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_word.append(word)
    
print("\nNumbers of palindromes found = {}\n".format(len(pali_word)))
print(*pali_word, sep= '\n')