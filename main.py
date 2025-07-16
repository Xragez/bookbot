from stats import get_book_text, count_words, count_characters

def main():
    book_contents = get_book_text('books/frankenstein.txt')
    # print(book_contents)
    num_words = count_words(book_contents)
    print(f"{num_words} words found in the document")
    char_dict = count_characters(book_contents)
    print(char_dict)

main()