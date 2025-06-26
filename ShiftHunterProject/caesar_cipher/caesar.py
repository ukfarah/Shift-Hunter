def caesar(text, shift, direction):
    alphabet = [chr(i) for i in range(97, 123)]  # a-z
    result = ""
    shift = shift % 26

    if direction == "decode":
        shift = -shift

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            base_char = char.lower()
            original_index = alphabet.index(base_char)
            new_index = (original_index + shift) % 26
            shifted_char = alphabet[new_index]
            result += shifted_char.upper() if is_upper else shifted_char
        else:
            result += char
    return result
