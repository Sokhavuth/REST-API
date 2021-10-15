#controllers/dashboard/category/create.py
import config, uuid
from bottle import request, redirect
from models.categorydb import createdb

def call():
    name = request.forms.getunicode('name')
    link = request.forms.getunicode('link')
    datetime = request.forms.getunicode('datetime')
    id = uuid.uuid4().hex

    createdb.call(name, link, datetime, id)

    return redirect('/dashboard/category')
