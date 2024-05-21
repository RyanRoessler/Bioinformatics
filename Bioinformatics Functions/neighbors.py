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