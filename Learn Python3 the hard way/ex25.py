def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') # split strings by whitespace。运算结果为一个list。此函数跟.strip()对应记。
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words) # sorted() creat a new ASC list, .sort() modify the existing list.

def print_first_word(words):
    """Prints the first word after popping it off. pop(): 取出对应的值，然后在原位置删除。"""
    word = words.pop(0) # remove and return the item at the given position in the list, default is the last one in the list.
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) # -1 is the default value for .pop()
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """SOrts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
