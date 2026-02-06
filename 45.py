def skill_match(req,can):
    return sum(req[k]*can[k] for k in req if k in can)
