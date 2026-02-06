def dataset_summary(data):
    return {
        "rows":len(data),
        "unique_values":{k:len({d[k] for d in data}) for k in data[0]}
    }
