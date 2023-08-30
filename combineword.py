print('Welcome to word combinations!')
word1 = input("Please enter the first word:")
word2 = input("Please enter the second word:")
wordspace = ('{: <1}'.format(word1))
wordspace2 = ('{: >1}'.format(word2))


def add(wordspace ,wordspace2):
    return(wordspace + wordspace2)
    
print(f"You're combined word is ... {add(wordspace, wordspace2)} ")