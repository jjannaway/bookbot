from stats import count_words
from stats import count_characters
from stats import sort_and_print_dict
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text(sys.argv[1])
    count = count_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    counted_characters = count_characters(text)
    sort_and_print_dict(counted_characters)
    print("============= END ===============")


main()