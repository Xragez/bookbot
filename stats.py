def get_book_text(filepath):
    with open(filepath, 'r') as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}

    for char in text:
        lowered_char = char.lower()

        if lowered_char not in characters:
            characters[lowered_char] = 1
        else:
            characters[lowered_char] += 1
    return characters

def get_char_count_list(characters):
    char_list = []
    for char, count in characters.items():
        if char.isalpha():
            char_list.append({
                'char': char,
                'num': count
            })
    char_list.sort(key=lambda x: x['num'], reverse=True)
    return char_list