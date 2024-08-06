
import re

def find_references(text):
    ref_matches = re.findall(r"\[(\d+)\]", text)
    
    ref_numbers = []
    for ref in ref_matches:
        ref_numbers.append(int(ref))
        
    return ref_numbers

example_text = "I recommend this book [1] but the other book [3] is better. Some people think that this website [10] is the best but I prefer this [7] one."

references = find_references(example_text)

print(references)
