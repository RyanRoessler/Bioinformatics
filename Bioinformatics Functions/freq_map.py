# Create a frequency map of k-mer pattern occurrences as a dictionary
def freq_map(seq, k):
    freqMap = {}
    # For the whole sequence - k
    for i in range(len(seq) - int(k) + 1):
        # Scanning window of letters (of length k)
        pattern = seq[i:i + int(k)]
        # For each new k-length segment, it sets its value to 1 in dictionary
        if pattern not in freqMap:
            freqMap[pattern] = 1
        # If k-length segment is already in dictionary, it increments its value (initially 1)
        freqMap[pattern] += 1
    return freqMap