# Finding Palingram Spells

### Finding and opening a dictionary

1. Whenever you load an external file, your program should automatically handle the I/O issues. So using  *try* and *except* to catch and handle *exceptions*.

   ```python
   try:
       with open(file) as in_file:
           # do something
   except IOError as e:
       print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
       sys.exit(1)
   ```

   * The *with* statement will automatically close the file after the nested block of code, regardless of  how the block exists.

   * Closing files prior to terminating a process is a good practice.

   * The ```sys.exit(1)``` is used to terminate the program. The ***1*** means that the program experiences an error and didn't close successfully.
   * If an exception couldn't match any named exception in the except clause, it is passed to any outer try statements or the main program execution. If no handler is found, the unhandled exception causes the program to stop with a standard “traceback” error message.

   ### Finding Palindromes
   
   Objective: Use Python to search English dictionary file for palindromes.
   
   Strategy: Identifying palindromes is easy: simply compare a word to itself sliced backward.
   
   ```python
   >>> word='NURSES'
   >>> word[:]
   'NURSES'
   >>> word[::-1]
   'SESRUN'
   ```
   
   
   
   More syntax
   
   1. splat operator (*) which takes a list as input and expands it into positional arguments in the function call.
   
   2. print() function separator parameter:  The default separator is a space (sep=''), but instead, print each item on a new line (sep='\n').
   
      ```python
      print(*pali_list, sep='\n')
      ```
   
   
   
   
   ### Finding Palingrams
   
   
A downside to using sets is that the order of the items in the set isn’t controllable and
duplicate values aren’t allowed. With lists, the order is preserved and duplicates are
allowed, but lookups take longer. Fortunately for us, we don’t care about order or
duplicates, so sets are the way to go!