# Hamming distance, or number of nucleotide mismatches between two strings of DNA
def hamming_distance(p, q):
    # Make sure the strings have the same length
    if len(p) != len(q):
        raise ValueError("Strings must have the same length")
    differences = 0
    # zip() takes iterables and returns tuples of the i-th element from each iterable
    for i, j in zip(p, q):
        if i != j:
            differences += 1
    return differences