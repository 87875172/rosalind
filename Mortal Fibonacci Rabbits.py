'''
class rabbit(object):
    def __init__(self, lifetime):
        self.lifetime = lifetime
        self.age = 1
      
    def reproduce(self):
        if 2 <= self.age < self.lifetime:
            total.append(rabbit(self.lifetime))
    
    def die(self):
        if self.age > self.lifetime:
            total.remove(self)

class population():
    def __init__(self, length):
        self.length = length
        
    def count(self):
        return len(total)
    
    def update(self):
        for j in xrange(self.length):
            for i in total:
                i.reproduce()
                i.die()
                i.age += 1
        
        #for k in total:
        #    k.reproduce()

total = [rabbit(3)]
som = population(15)
som.update()
print som.count()
'''

def rabbit_pairs(n, m):
    sequence = []
    for i in range(n):
        if i < 2:
            # Normal Fibonacci initialization
            total = 1
            sequence.append(total)
        elif (i < m) or (m == 0):
            # Normal Fibonacci calculation
            total = sequence[i - 1] + sequence[i - 2]
            sequence.append(total)
        elif i == m:
            # Now we need R(n - (m + 1)), but i - (m + 1) < 0, so we have to
            # provide the missing value
            total = sequence[i - 1] + sequence[i - 2] - 1
            sequence.append(total)
        else:
            # i - (m + 1) >= 0, so we can get the value from the sequence
            total = sequence[i - 1] + sequence[i - 2] - sequence[i - (m + 1)]
            sequence.append(total)
    return total

print rabbit_pairs(10, 5)

def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  print ages
  for i in xrange(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
    print ages
  return sum(ages)

print fib(10, 5)