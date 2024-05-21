# Find patterns that form (L,t)-clumps i.e., occurring t times within an L-nucleotide stretch
def find_clumps(seq, k, L, t):
    patterns = []
    for i in range(len(seq) - int(L) + 1):
        # Scanning window of length L
        window = seq[i:i + int(L)]
        # Get freqTable dictionaries of k-mers within L-length windows of sequence
        freqMap = freq_table(window, k)
        # For each item in dictionary
        for j in freqMap:
            # If value of key (counts) is t or higher, add to Patterns list
            if freqMap[j] >= int(t) and j not in patterns:
                patterns.append(j)
    patterns_nocommas = ' '.join(map(str, patterns))
    return patterns_nocommas