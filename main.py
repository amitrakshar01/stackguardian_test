from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import util

app = Flask(__name__)
api = Api(app)

# names = {"Book1": {"author": "Author1", "Release_Date": "01.01.2001", "isbn": 123456, "image": "Url1"},
#          "Book2": {"author": "Author2", "Release_Date": "02.02.2002", "isbn": 123465, "image": "Url2"},
#          "Book3": {"author": "Author3", "Release_Date": "03.03.2003", "isbn": 123654, "image": "Url1"},
#          "Book4": {"author": "Author4", "Release_Date": "04.04.2004", "isbn": 126354, "image": "Url1"},
#          "Book5": {"author": "Author5", "Release_Date": "05.05.2005", "isbn": 162354, "image": "Url1"},
#          "Book6": {"author": "Author6", "Release_Date": "06.06.2006", "isbn": 612354, "image": "Url1"}}

# class BookShelf(Resource):
#     def get(self, name):
#         return names[name]

# api.add_resource(BookShelf, "/bookshelf/<string:name>")

@app.route('/get_book_names', methods=['GET'])
def get_book_names():
    response = jsonify({
        'books': util.get_book_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    app.run(debug=True)
