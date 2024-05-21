from itertools import product

# Find the most frequently occurring mismatched patterns
    # This function returns the most frequent neighbor(s) AND a freqMap of all neighbors
def most_freq_mismatched_patterns(seq, k, d):
    neighbor_freqMap = {}
    most_freq_neighbors = []
    
    # Generate all theoretically possible neighbors
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

    # Find existing neighbors
    for nuc in range(len(seq) - int(k) + 1):
        # Sliding window of pattern length
        pattern = seq[nuc:nuc + int(k)]
        # Function call to generate neighborhood of all possible neighbors of a pattern with up to d mismatches
        neighborhood = neighbors(pattern, int(d))
        for neighbor in neighborhood:
            # Set all patterns = 0 in freqMap
            if neighbor not in neighbor_freqMap:
                neighbor_freqMap[neighbor] = 0
            # If pattern is found, increment in freqMap
            else:
                neighbor_freqMap[neighbor] += 1
                
    # Find most occurring k-mer with d or fewer mismatches and add it to patterns
    most_freq_neighbors = [neighbor for neighbor, freq in neighbor_freqMap.items() if freq == max(neighbor_freqMap.values())]
    # Most frequent neighbor(s), all neighbors
    return ' '.join(most_freq_neighbors), neighbor_freqMap