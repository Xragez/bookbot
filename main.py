from stats import get_book_text, count_words, count_characters, get_char_count_list
import sys

def print_report(filepath, book_contents):
    word_count = count_words(book_contents)
    characters = count_characters(book_contents)
    char_counts = get_char_count_list(characters)

    print("{============ BOOKBOT ============")
    print(f"Analyzing book found {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in char_counts:
        if char_dict['char'].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_contents = get_book_text(filepath)
    # print(book_contents)
    # num_words = count_words(book_contents)
    # print(f"{num_words} words found in the document")
    # char_dict = count_characters(book_contents)
    # print(char_dict)

    print_report(filepath, book_contents)

main()