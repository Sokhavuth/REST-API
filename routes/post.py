#routes/post.py
from bottle import Bottle, redirect
from controllers.login import checkLogged

import bottle
bottle.BaseRequest.MEMFILE_MAX = 1024 * 1024

app = Bottle()

@app.route('/', method='post')
def index():
    if checkLogged.call():
        from controllers.dashboard.post import create
        return create.call()
    else:
        redirect('/')

@app.route('/edit/<id>')
def index(id):
    if checkLogged.call():
        from controllers.dashboard.post import edit
        return edit.call(id)
    else:
        redirect('/')