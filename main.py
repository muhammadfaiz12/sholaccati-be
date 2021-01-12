from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory, jsonify
from db import init_db
from logic import show_chart_data, show_findings
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
db = init_db(app)

@app.route("/table")
def dashboard_table():
    filter = read_table_filter(request)
    print("WAHAHA")
    print(str(filter))
    res = show_findings(db, filter)
    return jsonify(res)

@app.route("/chart/<type>/<entity_name>/<semester>")
def chart_pie(type, entity_name, semester):
    res = show_chart_data()
    return jsonify(res)

def read_table_filter(request) -> dict:
    filter = {}

    list_of_filter = ["entity_name", "entity_type", "finding_amount_min", "finding_amount_max" "semester", "finding_type", "detail", "title"]
    for f in list_of_filter:
        filter_value = request.args.get(f)
        if filter_value is None:
            continue
        filter[f] = filter_value
    return filter

app.run()