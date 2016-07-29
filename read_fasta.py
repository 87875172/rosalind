def read_fasta(location):
    with open(location) as f:
        name = []
        se2 = []
        temp = ''
        
        for i in f:
            if i[0] == '>':
                name.append(i[1:-1])
                se2.append(temp)
                temp = '' 
                
            elif i[0] != '>':
                temp += i
        
        se2.append(temp)

        se2.pop(0)
        se = []
        
        for m in se2:
            se.append(m.replace('\n',''))
    return name, se