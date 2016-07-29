'''class Node(object):
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
'''
def gettree(location):
    f = open(location)
    n = f.readline()[:-1]
    edges = []
    for i in f:
        edges.append(i.split())
    return [n, edges]
'''
def cgraph(location):
    a,b = gettree(location)
    #print a, b
    nodes = []
    g = Digraph()
    
    for i in b:
        src = Node(i[0])
        dest = Node(i[1])
        if src not in nodes:
            nodes.append(src)
            g.addNode(src)
        if dest not in nodes:
            nodes.append(dest)
            g.addNode(dest)
        g.addEdge(Edge(src, dest))
        
    eds = []
    for i in str(g).split():
        eds.append(list(i.split('->')))
    return eds
#print a

def gnum(e):
    import copy
    
    a = copy.deepcopy(e)
    
    #a[0].append(123)
    #print 'a ' + str(a)
    #print 'e ' + str(e)
    for x in xrange(10):
        for i in xrange(len(e)):
            for j in xrange(len(e)):
                if e[j] and e[i]:
                    if e[j][0] in e[i] and e[j][1] not in e[i]:
                        #print e[i],e[j]
                        temp = copy.deepcopy(e)
                        #print temp
                        temp[i].append(e[j][1])
                        
                        flag = 0
                        for k in e:
                            #print 'temp[i] ' + str(temp[i])
                            #print 'k ' + str(k)
                            #print 'e ' + str(e)
                            if set(temp[i]) == set(k):
                                #print '=== temp[i] ' + str(temp[i])
                                #print '=== k ' + str(k)
                                #print '=== e ' + str(e)
                                flag = 1
                        if flag == 0:
                            #print e
                            e[i].append(e[j][1])
                            #print e
                            e[j] = []
                            temp = []
                        
                    elif e[j][1] in e[i] and e[j][0] not in e[i]:
                        temp = copy.deepcopy(e)
                        #print temp
                        temp[i].append(e[j][0])
                        #print temp
                        flag = 0
                        for l in e:
                            #print temp[i]
                            #print 'temp[i] ' + str(temp[i])
                            #print 'l ' + str(l)
                            if set(temp[i]) == set(l):
                                #print '=== temp[i] ' + str(temp[i])
                                #print '=== l ' + str(l)
                                #print str(temp[i]) + ' == ' + str(l)
                                flag = 1
                        if flag == 0:
                            #print str(temp[i]) + ' != ' + str(l)
                            e[i].append(e[j][0])
                            #print e
                            e[j] = []
                            temp = []
            
    #print 'a ' + str(a)
    #print 'e ' + str(e)
    if a == e:
        res = []
        for i in e:
            if i and list(set(i)) not in res:
                res.append(list(set(i)))
        return res
    else:
        #print 1
        return gnum(e)
a = cgraph('test.txt')
#print gnum(a)
'''
def main(location):
    a,b = gettree(location)
    #print a
    #print len(b)
    #c = cgraph(location)
    #print len(c)
    #temp = gnum(c)
    #print len(temp)
    #print temp
    '''res = []
    for i in temp:
        if len(i) > 1:
            #print i
            res.append(list(set(i)))
            #print list(set(i))
    #print len(res)
    fl = [item for sublist in res for item in sublist]
    #print fl
    #print len(res)
    #print len(fl)'''
    return int(a) - len(b) - 1

print main('rosalind_tree (1).txt')

'''
with open('rosalind_tree (1).txt') as input_data:
	edges = input_data.read().strip().split('\n')
	n = int(edges.pop(0))
	edges = [map(int,edge.split()) for edge in edges]

# List of sets of nodes which are connected to eachother.
# Initially start with completely disconnected nodes.
connected_nodes = [{i} for i in range(1,n+1)]

for edge in edges:
	temp_nodes = set()
	del_nodes = []
	for nodes in connected_nodes:

		# If both nodes in the edge are already connected, we're done.
		if (edge[0] in nodes) and (edge[1] in nodes):
			break

		# Check if only one end of the edge is in a given set of node.  If so, store the nodes.
		elif (edge[0] in nodes) or (edge[1] in nodes):
			# Add all the nodes to a temporary set.  Store the connected nodes for deletion.
			temp_nodes.update(nodes)
			del_nodes.append(nodes)
			# If we've found matches in two separate nodes, we're guaranteed to be done searching.
			if len(del_nodes) == 2:
				break

	# Check if an update is necessary.
	if len(del_nodes) != 0:
		# Make sure both nodes in the edge get added.
		temp_nodes.add(edge[0])
		temp_nodes.add(edge[1])
		# Remove the old connected nodes.
		for nodes in del_nodes:
			connected_nodes.remove(nodes)
		# Add one new connected node containing all the nodes.
		connected_nodes.append(temp_nodes)

print len(connected_nodes)-1
#with open('output/032_TREE.txt', 'w') as output_data:
#	output_data.write(str(len(connected_nodes)-1))
'''

