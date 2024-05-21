# The difference between the total number of occurrences of G and C in the first i nucleotides of Genome
def skew(genome):
    # Initialize cumulative sum
    skew_vals = [0]
    for nuc in genome:
        if nuc == 'C':
            # if C, subtract one from previous value
            skew_vals.append(skew_vals[-1] - 1)
        # if G, add one to previous value
        elif nuc == 'G':
            skew_vals.append(skew_vals[-1] + 1)
        # if A or T, simply retain the previous value
        else:
            skew_vals.append(skew_vals[-1])
    return skew_vals