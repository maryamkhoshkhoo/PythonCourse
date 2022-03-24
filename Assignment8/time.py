def sum(a,b):
    result = {}
    result['s'] = a['s'] + b['s']
    result['m'] = a['m'] + b['m']
    result['h'] = a['h'] + b['h']

    if result['s'] >=60:
        result['s']-=60
        result['m']+=1

    if result['m'] >=60:
        result['m']-=60
        result['h']+=1

    if result['h']>23:
        result['h']-=24

    return result

def sub(a,b):
    result = {}
    result['s'] = a['s'] - b['s']
    result['m'] = a['m'] - b['m']
    result['h'] = a['h'] - b['h']

    if result['s']<0:
        result['m']-=1
        result['s']+=60

    if result['m']<0:
        result['h']-=1
        result['m']+=60

    return result
     

def sec_to_time():
    second=int(input('Enter second: '))
    result = {}
    result['h'] = second // 3600
    result['m'] = (second % 3600) // 60
    result['s'] = (second % 3600) % 60
    return result

def time_to_sec():
    x = {}
    x['h'] = int(input('Enter hour: '))
    x['m'] = int(input('Enter minute: '))
    x['s'] = int(input('Enter second: '))
    second = ( int(x['h']) * 3600 ) + ( int(x['m']) * 60 ) + ( int(x['s']) ) 
    print(second)

def show(x):
    print(x['h'], ':', x['m'], ':', x['s'])

    
a  = {'h':2 , 'm':30 , 's':45}
b = {'h':3 , 'm':17 , 's':10}
 
     
c = sum(a,b)
show(c)


d = sub(a,b)
show(d)


e = sec_to_time()
show(e)


time_to_sec()