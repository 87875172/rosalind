up = 'GCGAGAGGGGACGGTCACACTCCTCCAGGATTAAAAATGGTCATCCTTATAAAGCACCGAGAGTTGGATCATCTTGAACGTTGCCTATCAGGATTCCAAGTCACAAGTTGGCAGGAGTCCGCTCCAATTGTATTTTGCCGTATACGAAGAACGAGGAGTGAAGTAAACGAAGATTACCGCACGTAGAGCGTGTAGGATCATGCCGAAATATACCGTTGGGCGCGGCGGGTGCGAGGCAAATCTATATCAGAAGGACGATGTTACTGTTTAGGGTTCGAAACGTCTGCTCGTAATCTTAGGGCAAAAAACACAGAGCAATCTGGACCAGCTACGGCCAGAAGGCTCGACCGTTCCACGTCCTATATCCCTCGGACGGTAAACACAGCCGTGTAATTCGGATAACCATCCAGCTACCGTGAAAGCGCCAGTATGCAGTTTACAAAGTCAAGTGAATCGGGGTGGGCTCAGACGGACAACCGCCCCGAGGTACTTAATAAACGCTTTAAGCCCATTATCGCGCTCAGTGCAGAACTAAATATAACACACCGGAGCCACACGGTACATAAGAACACATTTAGGACGTGCTAAAGACTCGATAATGTCTCTTGTGCATGGGTATTTTTCATGGTTCGTCAAAGCGACTGTTCCAGGTTAGTAGAATCTTCACTCTGGTGATGATCTGATTACGATGGTAAATGGCGTGCCAAACGCGAGGGACATGGGAGTAGGGGCAGCGGAGGTAGTCAGACTACCAACGCATCAACAGTGTGAGCAGGGGAGATGGTCTTGCAAGTGCTTCGCACTACACATCCCATCGCGATAATTGCAGTACACCCCATATAGTGGCCACTTATGTTTTAGTTCCCAAACTGGGAATTGTTGGTACGGCGGACGGCCTTTTGCAGTCG'
down = 'AAGAGTCGGGATGGGAACCCCGCTTAATCAATCCAAATGGGTTTCGTTCAAGGGCCTCGTAACCGGGAAATCCGGCACTAGTAGGCACTAGGATTCCGGTTCACAAGTTCGCTGGAGTCTCAGAGGAAAGCATGTGACAGTCAAATCGAAGAACGAACGCAGCTTGAGAAATATGAAGCAGAGTGGAGCGTGGAAGCCCCTGACTAGTATGAAGGTTCCTGTATATCGTCCAGGCGAGGAGCTACACAAACAGCACGGAGCAGCTGATTGCGGTGAGGAACCGCTGTACGGACACTTAACAATTAACTCATAGGCGAGTACGGACCCCCTAGGGTCCAGTAGTTAAAAAATTCTATGTCATAGCTCAGTCGCACGCGAAACGGAGAAGTGTAAGCTAAAAGAGCAGGGTGCGCAATGTCTAGCGATATTAATCAAATTTTGCTAATAATCCAATCGGGTTAGATTCTGAAAACCCGCCGACGCTCGTGACTTGATGAATGCCAGAAGCCCATTGTCGTTCTTTCGGTAGAAGAAAAGACATCAGCGCGTAGATTTTCGTTACGTACTCACCAATCTTAGACCGTCTCTAAGCAGACAGACCTAAACCTGACGGCCCCAATTTTACGCTGTTGTTCGACATCACTTTCCAGGGCAGGAACATTTTAAATCTTCCGCAGTAATGATTTTAGCGCTGCGTAGTCAGCCGAATGAATTGGAAATCTCGGTACGATAAACAGATGTCGTAAGAGAGCTAGCGAACTATCTGTATGTGACACTGAGATGTTAGAGGAACCACTTTCCACTTGACTTCCAGTTGCGGCAATTGTAATTAGAGCCACATTGTGGCCATCGATGTCGTACGTAACCTCCTGGTAATAGTTGTGTCGTGCTTCGGTTTCTCGTAATCC'

res = 0
for i in xrange(len(up)):
    if up[i] != down[i]:
        res += 1

print res