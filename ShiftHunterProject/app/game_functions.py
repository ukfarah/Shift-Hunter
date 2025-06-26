import random
import socket
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from caesar_cipher.caesar import caesar


def single_player_mode():
    word_category_map = {
        "hello": "greeting",
        "math": "school subject",
        "fun": "emotion",
        "logic": "school subject",
        "code": "tech term",
        "shift": "keyboard function",
        "hunter": "profession",
        "brain": "body part",
        "learn": "action",
        "try": "action",
        "lion": "animal",
        "banana": "fruit",
        "teacher": "profession",
        "planet": "space object",
        "river": "natural element",
        "flute": "instrument",
        "oxygen": "science"
    }
    secret_message = random.choice(list(word_category_map.keys()))
    category = word_category_map[secret_message]
    shift_key = random.randint(1, 25)
    encrypted_message = caesar(secret_message, shift_key, "encode")
    return encrypted_message, shift_key, secret_message, category

