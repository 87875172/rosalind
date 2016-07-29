name = []
se2 = []
temp = ''

with open('rosalind_grph.txt') as fasta:
    for i in fasta:
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

#print se,name

res = []

for i in xrange(len(name)):
    for j in xrange(len(name)):
        if se[j].startswith(se[i][-3:]) and i != j:
            res.append(name[i] + ' ' + name[j])

for i in res:
    print i