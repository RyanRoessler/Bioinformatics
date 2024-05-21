# Find the minimum skew position(s), where the reverse half-strand ends and the forward half-strand begins
def min_skew_positions(genome):
    skew_vals = skew(genome)
    min_skew_val = min(skew_vals)
    # Obtain all minimum skew value indices
        # enumerate() returns an index, value pair (i, skew) in the iterable (skew_val list)
    positions = [i for i, skew in enumerate(skew_vals) if skew == min_skew_val]
    return positions