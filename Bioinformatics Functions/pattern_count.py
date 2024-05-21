# Count the occurrences of a given pattern in a sequence
def pattern_count(seq, pattern):
    # Store 1 if pattern is encountered, and sum total
    return sum([1 for nuc in range(len(seq) - len(pattern)) if seq[nuc:nuc + len(pattern)] == pattern])