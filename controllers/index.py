#controllers/index.py
from bottle import Bottle, template, static_file, request


class Index(Bottle):
    def __init__(self):
        super().__init__()
        self.route('/static/images/<filename>', callback=self.loadImage)
        self.route('/static/styles/<filename>', callback=self.loadStyle)
        self.route('/static/scripts/<filename>', callback=self.loadScript)
        self.route('/static/fonts/<filename>', callback=self.loadFont)

        self.route('/', callback=self.index)

    def loadImage(self, filename):
        return static_file(filename, root='./asset/img')

    def loadStyle(self, filename):
        return static_file(filename, root='./asset/css')

    def loadScript(self, filename):
        return static_file(filename, root='./asset/js')

    def loadFont(self, filename):
        return static_file(filename, root='./asset/font')

    def checkLoggedIn(self, kdict):
        username = request.get_cookie('logged-in', secret=kdict['secretKey'])
        

    def index(self):
        return template('index', data={'title': 'Khmer Web REST API'})