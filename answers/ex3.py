
def count_word_match(words, match, case_sensitive):
    if not case_sensitive:
        # Make both the words and the match a consistent case
        words = words.casefold()
        match = match.casefold()

    word_list = words.split()

    count = 0
    for word in word_list:
        if word == match:
            count += 1

    return count

count1 = count_word_match("To be or not to be", "to", True)
print(count1)

count2 = count_word_match("To be or not to be", "to", False)
print(count2)
