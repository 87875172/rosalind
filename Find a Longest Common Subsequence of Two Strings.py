def readdata(location):
    with open(location) as f:
        a = f.readline()[:-1]
        b = f.readline()[:-1]
        print a
        print b
    return [a, b]

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

a = readdata('test.txt')
print long_substr(a)