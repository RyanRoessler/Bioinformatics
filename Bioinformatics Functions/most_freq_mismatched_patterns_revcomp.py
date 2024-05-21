# Import reverse_compliment() function
from reverse_compliment import reverse_compliment

# Finding the most frequent mismatched k-mers and obtaining their reverse compliments
    # This function returns the most frequent mismatched k-mer and its reverse compliment
def most_freq_mismatched_patterns_revcomp(seq, k, d):
    patterns = []
    freqMap = {}

    def neighbors(pattern, d):
        nucleotides = 'ACGT'
        neighborhood = set()
        # Positions in the pattern that could be mismatched: (0,0), (0,1), etc. if d=2
        for mismatched_indices in product(range(len(pattern)), repeat=d):
        # Result if pattern length=3 and d=2:
        # (0,0), (0,1), (0,2)
        # (1,0), (1,1), (1,2)
        # (2,0), (2,1), (2,2)
            
            # Nucleotide substitutions that will be applied: (A,A), (A,C), etc. if d=2
            for mismatches in product(nucleotides, repeat=d):
            # Result if pattern length=3 and d=2:
            # (A,A), (A,C), (A,G), (A,T)
            # (C,A), (C,C), ...
            # (G,A), ...
            # (T,A), ...
            
                neighbor = list(pattern)
                # Combine elements from mismatched_indices and mismatches as tuples: (0, A), (0, C), etc.
                for index, mismatch in zip(mismatched_indices, mismatches):
                    # Create mismatch substitutions
                    neighbor[index] = mismatch
                # All theoretically possible mismatches
                neighborhood.add(''.join(neighbor))
        return list(neighborhood)

    for nuc in range(len(seq) - int(k) + 1):
        pattern = seq[nuc:nuc + int(k)]
        # Generate the pattern's reverse compliment
        pattern_rc = reverse_compliment(pattern)
        neighborhood = neighbors(pattern, int(d))
        # Generate a neighborhood of reverse compliments
        neighborhood_rc = [reverse_compliment(n) for n in neighborhood]
        
        for neighbor in neighborhood + neighborhood_rc:
            if neighbor not in freqMap:
                freqMap[neighbor] = 1
            else:
                freqMap[neighbor] += 1

    max_freq = max(freqMap.values())
    patterns = [pattern for pattern, freq in freqMap.items() if freq == max_freq]
    return ' '.join(patterns)