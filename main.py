from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory, jsonify
from db import init_db
from logic import show_chart_data, show_findings

app = Flask(__name__)
db = init_db(app)

@app.route("/table")
def dashboard_table():
    res = show_findings()
    return jsonify(res)

@app.route("/chart/<type>/<entity_name>/<semester>")
def chart_pie(type, entity_name, semester):
    res = show_chart_data()
    return jsonify(res)

app.run()