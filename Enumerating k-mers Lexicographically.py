from itertools import product

def readdata(location):
    with open(location) as f:
        a = f.readline().split()
        b = int(f.readline())
    return a, b

def main():
    a, b = readdata('rosalind_lexf.txt')

    for i in product(a,repeat = b):
        print ''.join(i)

main()