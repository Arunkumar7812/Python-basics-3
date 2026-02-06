def build_vocab(sentences):
    return set(" ".join(sentences).lower().split())
