def main():
    books = "books/frankenstein.txt"
    text = get_book_text(books)
    count = get_word_count(text)
    chard = get_chars_dict(text)
    print("==========================")
    #print(text)
    print("==========================")
    print(f"Word count is {count}")
    print("==========================")
    print(chard)
    print("==========================")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(words):
    word_list = words.split()
    counter = 0
    for i in range(len(word_list)):
        counter += 1
    return counter

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
main()