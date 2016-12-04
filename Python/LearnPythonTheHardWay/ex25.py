
#before any manipulation of strings
#they muist be broken up and given 'index' values
def break_words(stuff):
    """This fuction will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints The frist words after popping it off.""" #people wanna popoff at the mouth
    #prints word at index position 0
    word = words.pop(0)
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    #prints the last word, or "first negative" word
    #think about this as being the word furthest form the top
    word = words.pop(-1)
    print word
def sort_sentence(sentence):
    """Takes in a full sentence and retuners the sorted words. """
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and lasts wors of the sentence. """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

