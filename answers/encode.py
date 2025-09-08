
import morse

message = "SOS We have hit an iceberg and need help quickly"  # Removed ! from end of string

try:
    encoded_message = morse.encode(message)

    print(f"Incoming message: {message}")
    print(f"   Morse encoded: {encoded_message}")
except ValueError as e:
    print(f"Could not encode message: {e}")
