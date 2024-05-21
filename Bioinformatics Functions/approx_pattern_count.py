# Count the number of approximate pattern occurrences
def approx_pattern_count(seq, pattern, d):
    positions = []
    for nuc in range(len(seq) - len(pattern) + 1):
        # Sliding window
        if hamming_distance_V2(pattern, seq[nuc:nuc + len(pattern)]) <= int(d):
            positions.append(nuc)
    return len(positions)