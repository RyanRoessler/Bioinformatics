# Convert the ASCII-encoded quality using "Phred+33"
def Q_to_Phred33(Q):
    # chr converts the ASCII character to its corresponding integer
    return chr(Q+33)

# Convert the quality integer to its ASCII-encoded character
def Phred33_to_Q(n):
    # ord reverse-converts integer to ASCII character
    return ord(n)-33