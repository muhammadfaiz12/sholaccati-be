from db import get_all_finding

def show_findings(db, filter: dict):
    print(str(filter))
    res = get_all_finding(db, filter)
    return res

def show_chart_data():
    return [{"chart1":"abc123"}]
