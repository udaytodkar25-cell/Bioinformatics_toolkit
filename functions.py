def similarity_percent(seq1, seq2):

    matches = ""
    count = ""
    for nuc1, nuc2 in zip(seq1, seq2):
            if nuc1 == nuc2:
                matches += nuc1
            Blank = "-"
            if nuc1 != nuc2:
                matches += Blank


    for i, nuc1 in zip(matches, seq1):
        if i == nuc1:
            count += i
    print(matches, len(count))


def ORF_finder(seq):
    start_codon = "ATG"
    stop_codon = "TAA", "TAG", "TGA"
    sequence = ""
    start_position = seq.find(start_codon)
    for i in range(start_position, len(seq) -2, 3):
        triplet = seq[i:i+3]
        print(triplet)
        sequence += triplet
        if triplet in stop_codon:
            break



def transcription(seq):
    trans = seq.replace("T", "U")
    print(trans)


def Translation(sequence):
    codon = ''
    seq = input("enter your sequence: ").upper()
    for nuc in range(0, len(seq) - 2, 3):
        codon = seq[nuc:nuc + 3]
        print(codon)
    triplets = [seq[i:i + 3] for i in range(0, len(seq) - 2, 3)]
    print(triplets)

    genes = {'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
             'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
             'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
             'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
             'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
             'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
             'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
             'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
             'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
             'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
             'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
             'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
             'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
             'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
             'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
             'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
             }
    proteins = ""
    for i in range(0, len(triplets)):
        if triplets[i] in genes:
            proteins = proteins + genes[triplets[i]]
    print(proteins)


def rev_complimentary(seq):
    seq = "ACTGACTG"

    reverse_complimentary = ""
    compliment = {"A": "U", "T": "A", "G": "C", "C": "G"}
    seqs = ""
    for i in seq:
        seqs = seq[::-1]
    print(seqs)
    for i in range(0, len(seqs)):
        reverse_complimentary = reverse_complimentary + compliment[seqs[i]]
    print(reverse_complimentary)


