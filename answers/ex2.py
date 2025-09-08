
def first_word(l):
    words = l.split()
    the_first_word = words[0]
    return the_first_word

sentence = "This is a collection of words"
word = first_word(sentence)
print(word)
