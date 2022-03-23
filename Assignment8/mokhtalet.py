def sum(x, y):
    result = {}
    result['r'] = x['r'] + y['r']
    result['i'] = x['i'] + y['i']
    return result

def sub(x, y):
    result = {}
    result['r'] = x['r'] - y['r']
    result['i'] = x['i'] - y['i']
    return result

def multi(x, y):
    result = {}
    result['r'] = ( x['r'] * y['r'] ) - ( x['i'] * y['i'] )
    result['i'] = ( x['i'] * y['r'] ) + ( x['r'] * y['i'] )
    return result

def show(x):
    print(x['r'] , ' + ', x['i'],'i' )
    
print('First complex number: ')
a1 = int(input("Please enter a: "))
b1 = int(input("Please enter b: "))
complex1 = { 'r' : a1, 'i': b1 }

print('Second complex number: ') 
a2 = int(input("Please enter a: "))
b2 = int(input("Please enter b: "))
complex2 = { 'r' : a2, 'i': b2 } 


sum = sum(complex1, complex2)
sub = sub(complex1, complex2) 
multi = multi(complex1, complex2) 



print('sum:', end=' ')
show(sum)

print('sub:' , end=' ')
show(sub)

print('multi:' , end=' ')
show(multi)