#controllers/dashboard/get.py
import config
from bottle import template
from copy import deepcopy

def call():
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​ជំពូក'
    kdict['route'] = 'category'

    return template('dashboard/index.tpl', data=kdict)
