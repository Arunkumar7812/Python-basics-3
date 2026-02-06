def dept_topper(students):
    top={}
    for s in students:
        d=s["dept"]
        if d not in top or s["marks"]>top[d]["marks"]:
            top[d]=s
    return top
