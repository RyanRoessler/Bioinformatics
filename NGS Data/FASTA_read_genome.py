# Read the genome sequence from a .fa file
def read_genome(file):
    genome = ''
    with open(file, 'r') as f:
        for line in f:
            # The first line of FASTA files begin with ">"
            # The second line is the start of the sequence
            if not line[0] == '>':
                genome += line.rstrip()
    return genome
