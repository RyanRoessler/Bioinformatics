# Retrieve the most frequent patterns in frequency table
def most_freq_patterns(seq, k):
    freqPatterns = []
    # Get freqMap dictionary
    freqMap = freq_table(seq, int(k))
    # For each pattern (key), count (value) item in dictionary
    for pattern, count in freqMap.items():
        # Find patterns with max count values
        if count == max(freqMap.values()):
            # Append freqPatterns list with those patterns
            freqPatterns.append(pattern)
    return freqPatterns