from stats import get_word_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book = get_book_text('./books/frankenstein.txt')
    num_words = get_word_count(book)
    print(f'{num_words} words found in the document')

main()
