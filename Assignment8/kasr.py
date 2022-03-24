def sum(a, b): 
    result = {}
    result['n'] = a['n'] * b['d'] + a['d'] * b['n']
    result['d'] = a['d'] * b['d']
    return result

def multi(a,b): 
    result = {}
    result['n'] = a['n'] * b['n'] 
    result['d'] = a['d'] * b['d']
    return result

def sub(a,b): 
    result = {}
    result['n'] = a['n'] * b['d'] - a['d'] * b['n']
    result['d'] = a['d'] * b['d']
    return result

def div(a,b):
    result = {}
    result['n'] = a['n'] * b['d'] 
    result['d'] = a['d'] * b['n']
    return result

def show(x): 
    print(x['n'], '/', x['d']) 

a = {'n':2 , 'd':3} 
b = {'n':4 , 'd':7} 

print("sum: ")
show(sum(a,b))

print("multi: ")
show(multi(a,b))

print("sub: ")
show(sub(a,b))

print("div: ")
show(div(a,b))  