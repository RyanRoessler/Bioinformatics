import random

# Randomly generate a DNA sequence of length n
def random_sequence(n):
    nucleotides = ['A', 'C', 'G', 'T']
    return ''.join(random.choice(nucleotides) for _ in range(n))