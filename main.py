from stats import get_num_words, get_chars_dict, chars_to_sorted_list
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_ch = chars_to_sorted_list(chars_dict)
    print_report(book_path, num_words, sorted_ch)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, sorted_ch):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_ch:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item["num"]}")
    print("============= END ===============")



main()

