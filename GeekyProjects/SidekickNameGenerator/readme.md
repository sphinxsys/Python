## The Objective
Randomly generate funny sidekick names

### Pseudocodes
* Load a list of firstnames
* Load a list of surnames

* Choose one firstname at random
* Assign the firstname to a variable
* Choose one surname at random
* Assign the surname to a varibale

* Print the combined names to the screen in order and in red font
* Ask user to quit or play again
* If user play again:
 repeat

* If user quit:
    end and exit


### Details
For the collection of firstnames & surnames, here we are using tuple instead of list. Why?

**tuple** _vs_ **list**:
The main deference between turple and list is that a list is mutable, whereas a tuple is immutable. This means that a list can be changed, but tuple cannot.

Then the syntax is a little different.
e.g.
```python
# Define a list with square brackets
list1 = [0, 1, 2, 3, 4]

# Define a tuple with parentheses
tuple1 = (1, 2, 3, 'abc')
```

Notice: Can't use a list as a key of a dictionary. Because only immutable value can be hashed. Hence, we can only set immutable values like tuple as keys

### Checking code with Pylint
Other such of programs like pycodestyle, Flake8 can easily help you to follow the PEP 8 style recommendations.
``` python
> pip install pylint
```
Then call `> pylint xxxx.py` to execute code

### Describe code with DocStrings
Here, in triple quotes, is an example of a single­line docstring for a function:

```python
def circ(r):
    """Return the circumference of a circle with radius of r."""
    c = 2 * r * math.pi
    return c
```

More complex example below:

```python
def circ(r):
    """Return the circumference of a circle with radius of r.

    Arguments:
    r – radius of circle

    Returns:
        float: circumference of circle
    """
    c = 2 * r * math.pi
    return c
```

Reference:
1. Google has its own format and style guide at https://google.github.io/styleguide/pyguide.html.

2. Examples of Google style can be found at https://sphinxcontribnapoleon.readthedocs.io/en/latest/example_google.html.

3. Details on Pylint are at https://docs.pylint.org/en/1.8/tutorial.html.

4. Details on pydocstyle can be found at http://www.pydocstyle.org/en/latest/.


### Practice Projects
1. Pig Latin
To form a Pig Latin, take a English word that begins with a consonant, move that consonant to the end, and then add "ay" to the end of the word. If the word begins with a vowel, then simply add "way" to the end of the word.

2. Poor Man's Bar Chart
Write a python script to take a sentence as input and returns a simple bar chart-type display
Hint: two modules will be used here --- "pprint" & "defaultdict" 