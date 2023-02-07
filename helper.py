from string import whitespace, punctuation, digits

punctuation = punctuation.replace('-','')

def validate(word):
    for char in word:
        if char in digits:
            print('Invalid word, no words contain digits! Try again.')
            return False
        if char in whitespace:
            print('Invalid word, no whitepsace allowed. Try again.')
            return False
        if char in punctuation:
            print('Invalid word, no punctuation allowed. Try again.')
            return False
    return True