from stats import get_word_count
from stats import count_characters
from stats import prepare_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    print('============ BOOKBOT ============')
    book = get_book_text('./books/frankenstein.txt')
    num_words = get_word_count(book)
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    c = count_characters(book)
    sorted_dict = prepare_dict(c)
    for thing in sorted_dict:
        if thing['character'].isalpha():
            print(thing['character'] + ': ' + str(thing['num']))
main()
