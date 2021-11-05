#controllers/dashboard/book/get.py
import config
from bottle import template
from copy import deepcopy

def call():
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​សៀវភៅ'
    kdict['route'] = 'book'

    return template('dashboard/index.tpl', data=kdict)