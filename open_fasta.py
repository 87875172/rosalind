

def open_fasta(location):
    sequence = []
    name = []
    temp = ''
    with open(location) as fasta:
        for i in fasta:
            if i[0] == '>':
                name.append(i[:-1])
                sequence.append(temp)
                temp = ''
            elif i[0] != '>':
                temp += i.replace('\n','')
    sequence.append(temp)
    return sequence[1:]
