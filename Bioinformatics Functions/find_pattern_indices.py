# Find locations of a k-mer pattern within a DNA sequence
def find_pattern_indices(seq, pattern):
    occurrences = []
    k = len(pattern)
    # For whole sequence - k
    for i in range(len(seq) - k + 1):
        # Checking for our pattern using a scanning window of size k 
        if seq[i:i + k] == pattern:
            # If our pattern is found, append the index to occurences list
            occurrences.append(i)
    occurrences_nocommas = ' '.join(map(str, occurrences))
    return occurrences_nocommas