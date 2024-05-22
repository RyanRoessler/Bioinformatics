class DNASequence:
    # Takes DNA sequence as argument
    def __init__(self, seq):
        # Converts seq to uppercase
        self.seq = seq.upper()
    
    def __len__(self):
        return len(self.seq)
    
    def nuc_count(self):
        nuc_counts = {'A':0, 'C':0, 'G':0, 'T':0}
        for nuc in self.seq:
            nuc_counts[nuc] += 1
        return nuc_counts
    
    def rev_comp(self):
        # Assign complimentary letters
        comp_dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
        # Replace each nucleotide with its complementary letter
        comp_seq = ''.join(comp_dict[n] for n in self.seq)
        # Reverse the entire string
        rev_comp_seq = comp_seq[::-1]
        return rev_comp_seq
    