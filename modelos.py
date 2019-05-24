import mysql as sql
from os import path

ROOT = path.dirname(path.relpath(__file__)))

def create_post(name, cantidad, price):
    con = sql.connect(path.join( ROOT, 'store.db')) 
    cur = con.cursor()
    cur.execute('insert into products ( name, quantity_in_stock, unit_price)  values ( ? , ? ,?)', (name, cantidad, price))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join( ROOT, 'store.db')) 
    cur = con.cursor()
    cur.execute('select * from products')
    posts = cur.fetchall()
    return posts