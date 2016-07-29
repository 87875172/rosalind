
'''
class Node(object):
    def __init__(self, name):
        self.name = str(name)
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

class Digraph(object):
    def __init__(self):
        self.nodes = set([])
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.add(node)
            self.edges[node] = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def childrenOf(self, node):
        return self.edges[node]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = ''
        for k in self.edges:
            for d in self.edges[k]:
                res = res + str(k) + '->' + str(d) + ' '
        return res[:-1]
    
class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)
        
    

#print a

#def edges(s):
    

#def perfect_matchings(s):
    
    #d = {'A':'U', 'U':'A', 'C': 'G', 'G':'C'}
    
    #mats = []
    
    
def edges(s):
    d = {'A':'U', 'U':'A', 'C': 'G', 'G':'C'}
    nodes = []
    for i in xrange(len(s)):
        nodes.append(Node(s[i] + str(i)))
    g = Digraph()
    
    for n in nodes:
        g.addNode(n)
    
    for i in xrange(len(nodes)):
        for j in xrange(i, len(nodes)):
            if d[(str(nodes[i]))[0]] == (str(nodes[j])[0]):
                g.addEdge(Edge(nodes[i], nodes[j]))
    return g

a = open_fasta('test.txt')[0]

def getnum(location):
    a = open_fasta(location)[0]
    c = str(edges(a))
    d = c.split()
    
    eds = []
    
    for i in d:
        eds.append(tuple(i.split('->')))
    
    matchings = []
    
    while eds:
        temp = []
        for i in xrange(len(eds)):
            for j in xrange(i, len(eds)):
                e = [item for sublist in temp for item in sublist]
                if eds[i][0] not in e and eds[i][1] not in e:
                    temp.append(eds[i])
                    eds = eds[1:]
        if temp not in matchings:
            matchings.append(temp)
    
    return matchings


print getnum('test.txt')'''

from math import factorial

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
    
a = open_fasta('rosalind_pmch.txt')[0]

print factorial(a.count("A")) * factorial(a.count("C"))

