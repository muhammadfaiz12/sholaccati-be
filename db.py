from flaskext.mysql import MySQL

# initialize DB
def init_db(app):
    mysql = MySQL()
    mysql.init_app(app)
    return mysql