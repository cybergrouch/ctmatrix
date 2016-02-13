def my_filter(L, num): return [ x for x in L if x % num != 0 ]

def my_list(L): return [ list(range(1, x+1)) for x in L ]

def my_function_composition(f, g): return { k:g[v] for k,v in f.items() }

def mySum(L):
    current = 0
    for x in L:
        current += x
    return current

def myProduct(L):
    current = 1
    for x in L:
        current *= x
    return current

def myMin(L):
    current = L[0]
    for x in L:
        current = ({x} if x < current else current)
    return current
    
def myConcat(L):
    current = ''
    for x in L:
        current += x
    return current
    
