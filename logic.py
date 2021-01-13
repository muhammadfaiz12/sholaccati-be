from db import get_all_finding, get_chart_info_pie
from bpk import *

def show_findings(db, filter: dict):
    print(str(filter))
    res = get_all_finding(db, filter)
    res = show_finding_search(res, filter)
    return res

def show_chart_data(db, filter: dict):
    result = []
    if filter["chart_type"] == "pie":
        if "semester" in filter.keys():
            result = get_chart_info_pie(db, filter['column'], filter['semester'])
        else:
            result = get_chart_info_pie(db, filter['column'], "")
        result = count_total_info_chart(result)

    elif filter["chart_type"] == "full":
        list_of_semester = ["2018-I", "2018-II", "2019-I", "2019-II", "2020-I"]
        results = []
        for s in list_of_semester:
            try:
                temp = get_chart_info_pie(db, filter['column'], s)
            except Exception:
                print("[ShowChartData] Error on processing semester "+s)
            temp = count_total_info_chart(temp)
            results.append(temp)
        result = results

    return result

def show_finding_search(res, filter: dict):
    result = []
    relevant_column = ["title" , "detail", "entity_name"]
    for c in relevant_column:
        if c in filter.keys():
            dataset = [(row,row[c]) for row in res]
            search_res = search_warper(filter[c], dataset)
            result = [x[0] for x in search_res] #0 because 1 is the grade
            res = result #for multi-filter search
    return res

def count_total_info_chart(result):
    total = 0
    for k in result.keys():
        if "total_amount" in k:
            continue
        try:
            total += int(result[k])
        except Exception as e:
            print("[COUNTTOTAL] exception happened when counting total for key "+ k)
    result["total"] = total
    return result


def search_warper(keyword, dataset):
    result = general_search(dataset, keyword)
    return result