def group_marks(marks):
    d={"<50":[],"50-74":[],">=75":[]}
    for m in marks:
        if m<50: d["<50"].append(m)
        elif m<=74: d["50-74"].append(m)
        else: d[">=75"].append(m)
    return d
