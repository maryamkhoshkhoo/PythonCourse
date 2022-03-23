def sum(x, y):
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

def sub(x, y):
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

def time_to_sec(time):
    second = ( time['h'] * 3600 ) + ( time['m'] * 60 ) + ( time['s'] )
    return second

def sec_to_time(time):
    result = {}
    result['h'] = time // 3600
    result['m'] = (time % 3600) // 60
    result['s'] = (time % 3600) % 60
    return result

def show(time):
    print(time['h'], ':', time['m'], ':', time['s'])
    
