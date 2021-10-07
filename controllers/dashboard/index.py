import config
from bottle import template
from copy import deepcopy

def call():
    kdict = deepcopy(config.kdict)
    kdict['siteLogo'] = 'ទំព័រ​គ្រប់គ្រង'

    return template('dashboard/index.tpl', data=kdict)
