#controllers/dashboard/index.py
import config
from bottle import template
from copy import deepcopy

def call():
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​ការផ្សាយ'
    kdict['route'] = 'index'

    return template('dashboard/index.tpl', data=kdict)
