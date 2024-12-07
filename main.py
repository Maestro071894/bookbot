def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = number_of_words(text)
    char_dict = count_characters(text)
    print(char_dict)


def number_of_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = {}

    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1

    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()