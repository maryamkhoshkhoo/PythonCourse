def sum(a, b):
    result = {}
    result['n'] = a['n'] * b['d'] + a['d'] * b['n']
    result['d'] = a['d'] * b['d']
    return result

def mul(a, b):
    result = {}
    result['n'] = a['n'] * b['n'] 
    result['d'] = a['d'] * b['d']
    return result

def sub(a, b):
    result = {}
    result['n'] = a['n'] * b['d'] - a['d'] * b['n']
    result['d'] = a['d'] * b['d']
    return result

def div(a, b):
    result = {}
    result['n'] = a['n'] * b['d'] 
    result['d'] = a['d'] * b['n']
    return result

def show(x):
    print(x['n'], '/', x['d'])

print('summation : ', end='')
show(sum)

print('subtraction : ' , end='')
show(sub)

print('multiplication : ' , end='')
show(mul)

print('division : ' , end='')
show(div) 