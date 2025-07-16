
def get_book_text(filepath):
    with open(filepath, 'r') as f:
        file_contents = f.read()
        return file_contents


def main():
    book_contents = get_book_text('books/frankenstein.txt')
    print(book_contents)


main()