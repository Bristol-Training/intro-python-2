
import refs

text = "I recommend this book [1] but the other book [3] is better. Some people think that this website [10] is the best but I prefer this [7] one."

numbers = refs.find_references(text)

expected = [1, 3, 10, 7]
if numbers == expected:
    print("Test passed")
else:
    print("Test failed:", numbers, "is not the same as", expected)
