def increments(L): return [ x+1 for x in L ]

def cubes(L): return [ x**3 for x in L ]

def tuple_sum(A, B): return [ (xa+xb,ya+yb) for ((xa,ya), (xb,yb)) in list(zip(A, B)) ]

def inv_dict(d): return { v:k for k,v in d.items() }

def row(p, n): return [ p+x for x in range(n) ]

def matrix(): return [ row(i, 20) for i in range(15) ]

def matrix2(): return [ [ i+x for x in range(20) ] for i in range(15) ]
