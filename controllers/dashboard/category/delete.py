#controllers/dashboard/category/delete.py
import config
from bottle import template, redirect
from models.categorydb import deletedb

def call(id):
    deletedb.call(id)
    
    redirect('/dashboard/category')
