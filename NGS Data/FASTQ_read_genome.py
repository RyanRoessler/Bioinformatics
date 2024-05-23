# Read the sequences and qualities of a FASTQ file
def FASTQ_read(file):
    sequences = []
    qualities = []
    with open(file) as f:
        while True:
            # Name line
            f.readline().rstrip()
            # Sequence line
            seq = f.readline().rstrip()
            # Placeholder
            f.readline().rstrip()
            # Qualities line
            qual = f.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities
