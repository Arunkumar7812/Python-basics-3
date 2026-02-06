def normalize_features(d):
    s=sum(d.values())
    return {k:v/s for k,v in d.items()}
