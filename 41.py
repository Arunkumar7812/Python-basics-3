def performance_index(students):
    res={s["name"]:s["marks"]*0.7+s["attendance"]*0.3 for s in students}
    return res, max(res,key=res.get)
