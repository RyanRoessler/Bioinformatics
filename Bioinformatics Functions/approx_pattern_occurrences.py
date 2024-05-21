# Finding all approximate occurrences of a pattern in a string (d or fewer mismatches from a given pattern)
def approx_pattern_occurrences(pattern, seq, d):
    pattern_len = len(pattern)
    seq_len = len(seq)
    positions = []
    # Sliding window
    for i in range(len(seq) - len(pattern) + 1):
        if hamming_distance_V2(pattern, seq[i:i + len(pattern)]) <= int(d):
            positions.append(i)
    return ' '.join(map(str, positions))