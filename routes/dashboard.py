#routes/dashboard.py
import config
from copy import deepcopy
from bottle import Bottle, redirect, template, request
from controllers.login import checkLogged

import bottle
bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024

app = Bottle()

@app.route('/')
def index():
    if checkLogged.call():
        from controllers.dashboard import index
        return index.call()
    else:
        redirect('/')

@app.route('/logout')
def logout():
    from controllers.dashboard import logout
    logout.call()

@app.route('/category')
def category():
    if checkLogged.call():
        from controllers.dashboard.category import get
        return get.call()
    else:
        redirect('/')

@app.route('/category', method='post')
def category_post():
    if checkLogged.call():
        from controllers.dashboard.category import create
        return create.call()
    else:
        redirect('/')

@app.route('/category/edit/<id>')
def category_edit(id):
    if checkLogged.call():
        from controllers.dashboard.category import edit
        return edit.call(id)
    else:
        redirect('/')