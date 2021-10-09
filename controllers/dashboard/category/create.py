#controllers/dashboard/category/create.py
import config
from bottle import template, request
from copy import deepcopy
from models.categorydb import createdb

def call():
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​ជំពូក'
    kdict['route'] = 'category'

    name = request.forms.getunicode('name')
    link = request.forms.getunicode('link')
    datetime = request.forms.getunicode('datetime')

    createdb.call(name, link, datetime)

    return redirect('dashboard/category')
