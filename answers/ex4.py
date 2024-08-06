
def find_references(text):
    words = text.split()
    
    refs = []
    # For each word in the text
    for word in words:
        # if it's surrounded by square brackets
        if word[0] == "[" and word[-1] == "]":
            # grab the bit between the square brackets
            reference = word[1:-1]
            # convert it to a number
            reference_number = int(reference)
            refs.append(reference_number)
    
    return refs

example_text = "I recommend this book [1] but the other book [3] is better. Some people think that this website [10] is the best but I prefer this [7] one."

references = find_references(example_text)

print(references)
