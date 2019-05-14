import pprint
from collections import defaultdict

def main():
    result = defaultdict(list)
    #chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','s','t','u','v','w','x','y','z']
    # for c in chars:
        # result[c]=0

    sentence = input("Please input a sentence: \n")
    
    for c in sentence:
        c = c.lower()
        if c.isalpha():
            result[c].append(c)
    
    print("Poor man's bar chart: \n")
    
    pprint.pprint(result)

if __name__ == '__main__':
    main()

