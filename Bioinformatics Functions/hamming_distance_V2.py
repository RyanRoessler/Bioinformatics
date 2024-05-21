# More efficient HammingDistance function using list comprehension
def hamming_distance_V2(p, q):
    if len(p) != len(q):
        raise ValueError("Strings must have the same length")
    return sum([1 for nuc in range(len(p)) if p[nuc] != q[nuc]])