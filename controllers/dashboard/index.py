#controllers/dashboard/index.py
import config
from bottle import template
from copy import deepcopy
from models.categorydb import getdb

def call():
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​ការផ្សាយ'
    kdict['route'] = 'index'

    kdict['categories'] = getdb.call('all')

    return template('dashboard/index.tpl', data=kdict)
