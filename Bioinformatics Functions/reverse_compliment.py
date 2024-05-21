# Obtaining the reverse compliment of a DNA sequence
def reverse_compliment(seq):
    # Assign complimentary letters
    comp_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    # Replace each nucleotide with its complementary letter
    comp_seq = ''.join(comp_dict[n] for n in seq)
    # Reverse the entire string
    rev_comp_seq = comp_seq[::-1]
    return rev_comp_seq