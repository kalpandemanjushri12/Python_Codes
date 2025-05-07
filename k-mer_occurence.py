def inpu():
    sequence=("atgtatgtagaca").upper()
    kmer=int(input("enter your k-mer:"))
    print("our sequence is:", sequence)
    print("length of seq is:",len(sequence))
    print("our k-mer sequences are:")
# by solving this formula we will get the no of k-mer grps we will get in output
    for i in range(len(sequence) - kmer + 1):
        print(i,sequence[i:i + kmer])
inpu() 
