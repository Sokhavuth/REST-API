#config.py
import os
#We need to install python-dotenv
from dotenv import load_dotenv

load_dotenv()
kdict = {}

kdict['SECRET_KEY'] = os.environ.get('SECRET_KEY')
kdict['DATABASE_URI'] = os.environ.get('DATABASE_URI')
