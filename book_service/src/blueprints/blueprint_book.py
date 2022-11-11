from flask import Blueprint,request,jsonify
from ..db import books_collection

blueprint_book = Blueprint(name='blueprint_book',import_name=__name__)

@blueprint_book.route('/add',methods=['POST'])
def add_book():
    books_collection.insert_one(request.get_json())
    return jsonify({'msg':'successfull'})
