#index.py
import sys
from routes import index
from routes import login

app = index.app
app.mount('/login', login.app)

if sys.platform == 'win32':
    app.run(host='localhost', port=7000, debug=True, reloader=True)