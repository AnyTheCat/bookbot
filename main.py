def main():
    books = "books/frankenstein.txt"
    text = get_book_text(books)
    count = get_word_count(text)
    print("==========================")
    print(text)
    print("==========================")
    print(f"Word count is {count}")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(words):
    word_list = words.split()
    counter = 0
    for i in range(len(word_list)):
        counter += 1
    return counter
    
main()