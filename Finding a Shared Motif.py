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

def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in xrange(len(data[0])):
            for j in xrange(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in xrange(len(data)):
        if find not in data[i]:
            return False
    return True

'''
def longestCommon(seqs):
  shortest = min(seqs, key=len)
  for length in xrange(len(shortest), 0, -1):
    for start in xrange(len(shortest) - length + 1):
      sub = shortest[start:start+length]
      if all(seq.find(sub) >= 0 for seq in seqs):
        return sub
  return ""
'''

a = open_fasta('rosalind_lcsm.txt')
print long_substr(a)