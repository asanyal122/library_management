from flask import Blueprint,request,jsonify
from ..db import books_collection
from bson.json_util import loads,dumps

blueprint_book = Blueprint(name='blueprint_book',import_name=__name__)

@blueprint_book.route('/',methods=['GET'])
def home():
    return jsonify({'msg':'successfull'})

@blueprint_book.route('/add',methods=['POST'])
def add_book():
    books_collection.insert_one(request.get_json())
    return jsonify({'msg':'successfull'})


@blueprint_book.route('/filter',methods=['GET','POST'])
def filter_book():
    if request.method == 'GET':
        books = list(books_collection.find())
        for book in books:
            book.pop('_id')
        return loads(dumps(books))
    elif request.method == 'POST':
        books=[]
        filter = {}
        print(dict(request.form))
        for key in request.form:
            filter[key]={'$regex':request.form[key]}
        print(filter)
        books = list(books_collection.find(filter))
        for book in books:
            book.pop('_id')
        return loads(dumps(books))


