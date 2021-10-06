#index.py
import sys
from controllers.index import Index  
    
if sys.platform == 'win32':
  app = Index()
  app.run(host='localhost', port=7000, debug=True, reloader=True)
else:
  app = Index()