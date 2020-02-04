def wheres_isaac(w):
    issac = []
    for vals in w.values():
        if isinstance(vals, str) and 'isaac' in vals:
            issac.append(vals)
    return issac

def find_issac_recursive(w):
    for i in w:
        if isinstance(i, str) and 'isaac' in i :
            return i

def list_or_dict(w):
    if isinstance(w, list):
        return find_issac_recursive(w)


    elif isinstance(w, dict):
        return wheres_isaac(w)

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
string_to_find = 'isaac'
f = 'ggssdsisaacjeej'
g = 'hwejdhfjewkhdue'
t = [4,5,6,7,'sdlfkisaacjsdf','hsa','dhdj',['pehfdje','behdisaacjb',['isaaca',{'Hero':'isaac-man'}]]]
e = {'Name': "isaac"}
# print(list_or_dict(gift_list))
##############################

def really_recursive(a):
    if isinstance(a, str) and string_to_find in a:
        print(a)

    if isinstance(a, list):
        for i in a:
            really_recursive(i)
    
    if isinstance(a, dict):
        for val in a.values():
            really_recursive(val)
                

# really_recursive(f)
# really_recursive(g)
really_recursive(t)
really_recursive(e)