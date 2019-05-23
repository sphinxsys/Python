import load_dictionary

word_list = load_dictionary.loadfile('2of4brif.txt')

anagram_list = []

# Input a single name 
name = 'Foster'
print('Input name =  {}'.format(name))

name = name.lower()
print('Using name = {}'.format(name))

# sort the name & find anagrams
name_sorted = sorted(name)

for word in word_list:
    if len(word) == len(name_sorted) and name_sorted == sorted(word):
        anagram_list.append(word)

# print out the list
if len(anagram_list) == 0:
    print('You need a larger dictionary or a new name!')
else:
    print('Anagrams = ', *anagram_list, sep='\n')