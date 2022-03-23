def sum(x,y):
    result = {}
    result['s'] = x['s'] + y['s']
    result['m'] = x['m'] + y['m']
    result['h'] = x['h'] + y['h']

    if result['s'] >=60:
        result['s']-=60
        result['m']+=1

    if result['m'] >=60:
        result['m']-=60
        result['h']+=1

    if result['h']>23:
        result['h']-=24

    return result

def sub(x,y):
    result = {}
    result['s'] = x['s'] - y['s']
    result['m'] = x['m'] - y['m']
    result['h'] = x['h'] - y['h']

    if result['s']<0:
        result['m']-=1
        result['s']+=60

    if result['m']<0:
        result['h']-=1
        result['m']+=60

    return result

def time_to_sec():
    second = ( x['h'] * 3600 ) + ( x['m'] * 60 ) + ( x['s'] )
    return second

def sec_to_time():
    result = {}
    result['h'] = x // 3600
    result['m'] = (x % 3600) // 60
    result['s'] = (x % 3600) % 60
    return result

def show(x):
    print(x['h'], ':', x['m'], ':', x['s'])
    
x  = {'h':2 , 'm':30 , 's':45}
y = {'h':3 , 'm':17 , 's':10}

show(sum(x,y))
show(sub(x,y))
show(time_to_sec())
show(sec_to_time(9045)) 


