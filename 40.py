def is_consistent(data):
    keys=data[0].keys()
    return all(d.keys()==keys for d in data)
