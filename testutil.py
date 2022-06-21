import json


global __books
    
def get_book_names():
    with open("./names.json", "r") as f:
        __books = json.load(f)['books']
    return __books

if __name__ == '__main__':
    print(get_book_names())