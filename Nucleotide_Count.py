def count_nucleotide(dna_string):
    a_count = dna_string.count('A')
    c_count = dna_string.count('C')
    g_count = dna_string.count('G')
    t_count = dna_string.count('T')
    print(a_count,c_count,g_count,t_count)
dna_string =input("enter your nucleotide sequence:").upper()
print("Nucletide sequence is:",dna_string)
count_nucleotide(dna_string)
