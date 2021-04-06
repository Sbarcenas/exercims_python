def proteins(strand):
    i = 0
    proteins = dict(
        AUG="Methionine",
        UUU="Phenylalanine",
        UUC="Phenylalanine",
        UUA="Leucine",
        UUG="Leucine",
        UCU="Serine",
        UCC="Serine",
        UCA="Serine",
        UCG="Serine",
        UAU="Tyrosine",
        UAC="Tyrosine",
        UGU="Cysteine",
        UGC="Cysteine",
        UGG="Tryptophan",
        UAA="STOP",
        UAG="STOP",
        UGA="STOP"
    )

    output = list()
    while i < len(strand):
        current = strand[i:i + 3]
        i = i + 3

        protein_val = proteins[current]

        if protein_val == 'STOP':
            break
        else:
            output.append(protein_val)

    return output