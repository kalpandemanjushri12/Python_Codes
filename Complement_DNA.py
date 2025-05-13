def compl_dna():
    dna_seq = input("Enter your dna sequence:").upper()
    print("the dna sequence is :",dna_seq)
    print("the complement of dna sequence is:")
    for nucleotide in dna_seq:
        if nucleotide == "A":
            print("T",end = "")
        elif nucleotide == "T":
            print("A",end = "")
        elif nucleotide == "G":
            print("C", end = "")
        elif nucleotide == "C":
            print("G",end="")
        else:
            print("N",end="") 
compl_dna()
