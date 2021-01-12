from flaskext.mysql import MySQL

# initialize DB
def init_db(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'sholaccati'
    mysql = MySQL(app)
    return mysql