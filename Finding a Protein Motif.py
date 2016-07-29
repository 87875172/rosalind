import urllib

se2 = []
name = []
temp = ''

with open('rosalind_mprt.txt') as sample:
    for i in sample:
        urllib.urlretrieve ("http://www.uniprot.org/uniprot/" + i[:-1] + ".fasta", i[:-1] + ".txt")

        with open(i[:-1] + '.txt') as fasta:
            for j in fasta:
                if j[0] == '>':
                    name.append(i[:-1])
                elif j[0] != '>':
                    temp += j.replace('\n','')
        
            se2.append(temp)
            temp = ''

#se2.pop(0)
#se = []

#for m in se2:
#    se.append(m.replace('\n',''))

#print se2,name

Ngly = []
for i in xrange(len(name)):
    Ngly.append([])

#print Ngly
#print se2
#print len(se2[1])
#print se2

for k in xrange(len(name)):
    for l in xrange(len(se2[k]) - 4):
        #print se2[i]
        if se2[k][l] == 'N' and se2[k][l+1] != 'P' and (se2[k][l+2] in 'ST') and se2[k][l+3] != 'P':
            Ngly[k].append(l+1)
            #print l+1

#print Ngly
res = ''

for m in xrange(len(Ngly)):
    if Ngly[m] != []:
        #print Ngly[m]
        print name[m]
        for n in Ngly[m]:
            res += str(n) + ' '
        print res
        res = ''
