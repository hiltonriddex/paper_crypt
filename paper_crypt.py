"""
File: paper_crypt.py
Author: Hilton Riddex
Date Created: 26/03/2025
Version: 1.0
Description: This script implements a paper/pen based encryption algorithm that is relative secure.
Usage: python paper_crypt.py
"""

def create_char_map():
    """Creates a dynamic character-to-number mapping."""
    char_map = {}
    letters = 'abcdefghijklmnopqrstuvwxyz'
    special_chars = ',. . ? '
    all_chars = letters + special_chars
    
    low = 1
    high = len(all_chars)
    
    for char in all_chars:
        if low <= high:
            if letters.find(char) != -1: # letter
                if low % 2 == 1:
                    char_map[char] = high
                    high -= 1
                else:
                    char_map[char] = low
                    low += 1
            else: # special char
                if low % 2 == 1:
                    char_map[char] = high
                    high -= 1
                else:
                    char_map[char] = low
                    low += 1

    return char_map

def process_string(input_string, char_map):
    """Converts a string to a list of numbers."""
    input_string = input_string.lower()
    return [char_map[char] for char in input_string if char in char_map]

def encrypt(message, key, char_map):
    """Encrypts the message using the key."""
    message_numbers = process_string(message, char_map)
    key_numbers = process_string(key, char_map)
    encrypted_numbers = []
    for i in range(len(message_numbers)):
        encrypted_numbers.append(message_numbers[i] + key_numbers[i % len(key_numbers)])
    return encrypted_numbers

def decrypt(encrypted_numbers, key, char_map):
    """Decrypts the message using the key."""
    key_numbers = process_string(key, char_map)
    decrypted_numbers = []
    for i in range(len(encrypted_numbers)):
        decrypted_numbers.append(encrypted_numbers[i] - key_numbers[i % len(key_numbers)])

    reverse_char_map = {v: k for k, v in char_map.items()}
    decrypted_message = ''.join(reverse_char_map[num] for num in decrypted_numbers if num in reverse_char_map)
    return decrypted_message

# Example usage
char_map = create_char_map()
message = "Hello, World?"
key = "MySecretKeyAnyStringFromAnywhere"

encrypted_message = encrypt(message, key, char_map)
print("Encrypted:", encrypted_message)

decrypted_message = decrypt(encrypted_message, key, char_map)
print("Decrypted:", decrypted_message)