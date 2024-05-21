# Faster/more efficient code for longer genomes
def find_clumps_V2(seq, k, L, t):
    patterns = set()
    # Make one freqMap dictionary, default key values = 0
    freqMap = defaultdict(int)
    # Add each pattern to freqMap for first window
    for nuc in range(L):
        pattern = seq[nuc:nuc + k]
        freqMap[pattern] += 1
        if freqMap[pattern] == t:
            patterns.add(pattern)
    # Slide the window and update the frequency table incrementally
    for nuc in range(1, len(seq) - L + 1):
        old_pattern = seq[nuc - 1:nuc - 1 + k]
        # Decrement the k-mer that exited to avoid double counts in the current window
        freqMap[old_pattern] -= 1
        new_pattern = seq[nuc + L - k:nuc + L]
        # Increment the new k-mer that entered window
        freqMap[new_pattern] += 1
        if freqMap[new_pattern] == t:
            patterns.add(new_pattern)
    return list(patterns)