import json

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global  __data_columns
    global __books

    with open("./names.json", "r") as f:
        __data_columns = json.load(f)['books']
    
    print("loading saved artifacts...done")

def get_book_names():
    return __books

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_data_columns())