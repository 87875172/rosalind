fasta = open('rosalind_gc (2).txt')

name = []
se2 = []
temp = ''

for i in fasta:
    if i[0] == '>':
        name.append(i[1:-1])
        se2.append(temp)
        temp = '' 
        
    elif i[0] != '>':
        temp += i

se2.append(temp)
fasta.close()
se2.pop(0)
se = []

for m in se2:
    se.append(m.replace('\n',''))

p = []

for j in se:
    counter = 0.0
    for k in j:
        if k == 'G' or k == 'C':
            counter += 1
    p.append(counter/len(j))

ma = 0
ind = 0
for l in xrange(len(p)):
    if p[l] > ma:
        ma = p[l]
        ind = l
#print name, p
print se
print name[ind], max(p)*100