from stats import get_num_words
from stats import get_char_count
from stats import sorting_dict
import sys

if len(sys.argv) < 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_chars = sorting_dict(char_count)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print(f"--------- Character Count -------")
    for char_dict in sorted_chars:
        character = char_dict["char"]
        count = char_dict["count"]
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

    





main()
