# Generates all possible neighbors of a pattern with d or fewer mismatches
def neighbors_V2(pattern, d):
    from hamming_distance_V2 import hamming_distance_V2
    nucleotides = 'ACGT'
    
    # Case: d = 0
    if d == 0:
        return {pattern}
    # Case: pattern is 1 letter
    if len(pattern) == 1:
        return set(nucleotides)

    # Case: d > 0 and pattern > 1 letter
    neighborhood = set()
    # Starting with possible mismatches at the first letter, keeping the suffix of the pattern the same
    # Then, use recursion to iterate over all possible mismatches at each remaining letter index
    suffix_neighbors = neighbors_V2(pattern[1:], d)

    for neighbor in suffix_neighbors:
        # If the Hamming distace of the suffix is < d, the neighbor differs by at most d mismatches
        if hamming_distance_V2(pattern[1:], neighbor) < int(d):
            for nucleotide in nucleotides:
                # Concatenate each of the four nucleotides to the suffix of the pattern
                neighborhood.add(nucleotide + neighbor)
        else:
            neighborhood.add(pattern[0] + neighbor)
    return list(neighborhood)