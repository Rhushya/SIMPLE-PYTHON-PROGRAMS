import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

print(generate_password(12))  # Example output: 'aB1#eF2@hJ8!'
