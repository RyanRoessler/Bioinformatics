# Find (k,d)-motifs in a given collection of DNA sequences
    # The motifs/neighbors must be present in all sequences/strings
    # This function uses a given collection DNA sequences separated by spaces (Dna)
def motif_enumeration(Dna, k, d):
    from hamming_distance_V2 import hamming_distance_V2
    from neighbors_V2 import neighbors_V2
    patterns = set()
    # For each DNA sequence - k substring
    for nuc in range(len(Dna[0]) - int(k) + 1):
        # Sliding window of length k to find all patterns in each sequence
        pattern = Dna[0][nuc:nuc + int(k)]
        # Get all possible neighbors of each pattern in sliding window
        pattern_neighbors = neighbors_V2(pattern, d)
        motifs_found = set()
        # For each neighbor in the set of all possible neighbors for all patterns across all sequences
        for neighbor in pattern_neighbors:
            is_motif = True
            # Check each DNA sequence for the current neighbor
            for seq in Dna:
                motif_found = False
                # Check current DNA sequence substring
                for nuc in range(len(seq) - int(k) + 1):
                    # If the number of mismatches is d or fewer in a sliding window of patterns
                    if hamming_distance_V2(neighbor, seq[nuc:nuc + int(k)]) <= int(d):
                        # Motif found and move to the next substring in the current sequence
                        motif_found = True
                        # Break and go to next DNA sequence
                        break
                if not motif_found:
                    is_motif = False
                    break
            # After all sequences are parsed, if still true, neighbor was found in all sequences, so add that motif to "motifs_found" set
            if is_motif:
                motifs_found.add(neighbor)
        patterns.update(motifs_found)
    return ' '.join(list(set(patterns)))