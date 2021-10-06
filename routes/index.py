#routes/index.py
from bottle import Bottle, template, static_file, request, response

app = Bottle()

@app.route('/static/images/<filename>')
def loadImage(filename):
    return static_file(filename, root='./asset/img')


@app.route('/static/styles/<filename>')
def loadStyle(filename):
    return static_file(filename, root='./asset/css')


@app.route('/static/styles/partials/<filename>')
def loadStylePartial(filename):
    return static_file(filename, root='./asset/css/partials')


@app.route('/static/scripts/<filename>')
def loadScript(filename):
    return static_file(filename, root='./asset/js')


@app.route('/static/scripts/ckeditor/<filename>')
def loadCKEditorScript(filename):
    return static_file(filename, root='./asset/js/ckeditor')


@app.route('/static/fonts/<filename>')
def loadFont(filename):
    return static_file(filename, root='./asset/font')


@app.route('/')
def index():
    return template('index', data={'title': 'Khmer Web REST API'})