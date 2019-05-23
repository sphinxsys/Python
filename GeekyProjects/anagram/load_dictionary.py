""" Load dictionary file 


    Arguments:
    - the txt file name (add path if needed)

    Exception:
    IOError if the file doesn't exist

    Returns:
    A list of all words from txt file in low case

    Require:
    import sys

"""


import sys

def loadfile(file):
    """ Load file and return a list of lowercase strings """
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [x.lower() for x in loaded_text]
            return loaded_text
    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)