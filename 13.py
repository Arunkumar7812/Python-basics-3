def unique_tuple_pairs(lst):
    return list({tuple(sorted(t)) for t in lst})
