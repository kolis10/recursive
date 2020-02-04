


gift_list = {
    'Name':"Hernan",
    'Relation':"Issac's Smug Teacher",
    'Gift1':"coal",
    'Gift2':"bad review from Issac",
    'Gift3':"Wendys gift card from Issac",
    'sdf':"kkisaacd",
    'dlk':432,
    '324':"dslkisaacl",
    'dflkj':2343
}

def wheres_isaac(w):
    issac = []
    for vals in w.values():
        if isinstance(vals, str) and 'isaac' in vals:
            issac.append(vals)
    return issac

# print(wheres_isaac())
######################################
t = [4,5,6,7,'sdlfkisaacjsdf','hsa','dhdj']
l = {'lk','sodf',34,345,'dfisaaclkj'}
g = {'asdf':1, 'lk': 'ldfisaacfsd'} 
obj = {
    'sdf':345,
    'lk': 'asdf',
    'sdyu': t
}
x = 'sdlfkisaacjsdf'
m = [3,4,5,6,7,'isaac']
y = {'one':1, 'two':2, 'three':x}



def find_issac_recursive(w):
    for i in w:
        if isinstance(i, str) and 'isaac' in i :
            return i



def list_or_dict(w):
    if isinstance(w, list):
        return find_issac_recursive(w)


    elif isinstance(w, dict):
        return wheres_isaac(w)
     

# print(4 in m)
# print('isaac' in x)
# print(find_issac_recursive())
# print(find_list(y))
# print(find_dict(y))
print(list_or_dict(x))
