
from morse import Message

my_message = Message("hello world")
morse_string = my_message.as_morse()

incoming_message = Message(morse_string)
decoded_string = incoming_message.as_english()

print(decoded_string == "hello world")
