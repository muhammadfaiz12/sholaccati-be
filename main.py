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

@app.route("/chart")
def chart_pie():
    filter = read_chart_filter(request)
    if "chart_type" not in filter.keys() or "column" not in filter.keys():
        return jsonify("invalid request: no chart_type and/or column information received")
    res = show_chart_data(db, filter)
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

def read_chart_filter(request) -> dict:
    filter = {}
    list_of_filter = ["chart_type", "column", "semester"]
    for f in list_of_filter:
        filter_value = request.args.get(f)
        if filter_value is None:
            continue
        filter[f] = filter_value
    return filter

app.run()