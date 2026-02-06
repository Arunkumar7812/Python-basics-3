def vocab_coverage(exp,docs):
    used=set(" ".join(docs).split())
    return len(used&exp)/len(exp)*100, exp-used
