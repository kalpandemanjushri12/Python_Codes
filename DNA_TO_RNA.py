dna_seq = input("enter sequence:").upper()
print("The DNA sequence is:",dna_seq)
#defining transcription
def transcription(dna_seq):
    rna_seq=""
    for nucleotide in dna_seq:
        if nucleotide == 'A':
            rna_seq=rna_seq+nucleotide
        elif nucleotide == 'T':
            rna_seq=rna_seq+'U'
        elif nucleotide == 'G':
            rna_seq=rna_seq+nucleotide
        elif nucleotide == 'C':
            rna_seq=rna_seq+nucleotide
        else:
            rna_seq = rna_seq + nucleotide
    return rna_seq
rna_seq = transcription(dna_seq)
print("your converted dna to rna-seq is:",rna_seq)
