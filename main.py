from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory
from db import init_db

app = Flask(__name__)
db = init_db(app)

@app.route("/table")
def dashboard_table():
    pass

@app.route("/chart/<type>/<entity_name>/<semester>")
def chart_pie():
    pass

app.run()