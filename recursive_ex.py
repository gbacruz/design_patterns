recursivi = [2,3,4,5,200,0,910,1988,9878]
def recurser(params=[]):
    if len(params)==0:
        return None
    else:
        print(params[0]*2,params[0])
        recurser(params[1:])
recurser(recursivi)