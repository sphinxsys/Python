""" Find all word-pair palingrams in a dictionary file """
import load_dictionary

word_list = load_dictionary.loadfile('2of4brif.txt')

# find word-pair palingrams
def findPalingrams():
    """ Find dictionary palingrams """
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]

        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i], word))
    
    return pali_list

palingrams = findPalingrams()

# sort palingrams on the first word
palingrams_sorted = sorted(palingrams)

# display the palingrams
print("\nNumber of palingrams = {} \n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))
                    