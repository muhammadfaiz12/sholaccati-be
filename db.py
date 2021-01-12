from flaskext.mysql import MySQL

# initialize DB
def init_db(app):
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'sholaccati'
    mysql = MySQL(app)
    return mysql

def append_query_with_filter(query:str, filter: dict):
    query += " where "
    for f in filter:
        if "finding_amount" in f:
            query += "finding_amount >= {0} and finding_amount <= {1} ".format(filter["finding_amount_min"], filter["finding_amount_max"])
        else:
            query += "{0} = '{1}' ".format(f, filter[f])
    query += ";"
    return query

def get_all_finding(mysql, filter: dict):
    cursor = mysql.get_db().cursor()
    query = 'SELECT id, entity_name, entity_type, finding_amount, semester, finding_type, detail, title FROM findings'
    if len(filter.keys()) > 0:
        query = append_query_with_filter(query, filter)
    print(query)
    cursor.execute(query)
    accounts = cursor.fetchall() 
    res = []
    for acc in accounts:
        temp = {
            "id": acc[0],
            "entity_name": acc[1],
            "entity_type": acc[2],
            "finding_amount": acc[3],
            "semester": acc[4],
            "finding_type": acc[5],
            "detail": acc[6],
            "title":acc[7]
        }
        res.append(temp)
    return res