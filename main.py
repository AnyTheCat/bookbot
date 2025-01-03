def main():
    books = "books/frankenstein.txt"
    text = get_book_text(books)
    print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()