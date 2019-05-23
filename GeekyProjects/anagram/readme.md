# Solving Anagrams

An anagram is a word formed by rearranging the letters of other word.

e.g.

***Elvis*** ==> ***lives*** or ***veils***, ***evils***

### Project #1 Finding Single-Word Anagrams

**The Objective**: Use Python and a dictionary file to find all the single-word anagrams for a given English word or single name. 

**The Strategy & Pseudocode**:  The key of the problem -- the anagrams have the same number of the same letters.

1. Same length;

2. Instead of retreating two words as two string, regard them as two lists containing single-character strings. 

```python
> word=sorted(word)
> word
['o', 'p', 's', 't']
> anagram=sorted(anagram)
> anagram
['o', 'p', 's', 't']
> anagram==word
True
```

   **Pseudocode**:

+ Load dictionary file as a list of words
+ Accept a word from user
+ Create an empty list to hold anagrams
+ Sort the user-word
+ Loop through each word in the word list:

  + Sort the word

  + if word sorted is equal to user-word sorted:

    + Append word to anagrams list

+ Print anagrams list

### Project #2 Finding Phrase Anagrams

**The Objective**:  Write a Python program that lets a user interactively build an anagram phrase from the letters in the name.

**The Strategy & Pseudocode**: A strategic challenge here: how does a computer handle contextual content?  

The brute-force method is a common approach used in online anagram generators. But most of the returned phrases are nonsense.

So an alternative approach is to acknowledge that humans are best at contextual issues and write a program that helps the human work through the problem. "word by word"

Python ships with a module named *collection* that includes several container data types. One of these types, *counter*, counts the occurrences of an item. 

***Note***: In python, the dictionary is unsorted, but Python correctly identifies each dictionary as being equal if the dictionaries contain the same keys and the same values.

***Pseudocode***:
2 design decisions: 
(1) let the user interactively build their anagram one word at a time;
(2) use the ***Counter*** method to find anagrams.
Load a dictionary file
Accept a name from user
Set Limit = length of name
Start empty list to hold anagram phrase
While length of phrase < limit:
	Generate list of dictionary words that fit in name
	Present words to user
	Present renaming letters to user
	Present current phrase to user
	Ask user to input word or start over
	If user input can be made from remaining letters:
		Accept choice of new word or words from user
		Remove letters in choice from letters in name
		Return choice and remaining letters in name
	If choice is not a valid selection:
		Ask user for new choice and remaining letters in name
	Add choice to phrase and show to user
	Generate new list of words and repeat process
When phrase length equal limit value:
	Display final phrase
	Ask user to start over or to exit

***Tips***: When draw flowchart, marking the different steps in the different color will be helpful to locate the different method and scope.

​    

