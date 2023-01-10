import random as rd 

setfirst = set()
setlast = set()
with open('first_names.txt') as first :
    with open('last_names.txt') as last : 
        for line in first : 
            setfirst.add(str(line.rstrip()))
        for line in last : 
            setlast.add(str(line.rstrip()))

people = set()
data = set()
while len(people)<10000 : 
    new_ppl = rd.sample(setfirst, 1)[0] + ' ' + rd.sample(setlast, 1)[0]
    if new_ppl not in people :
        people.add(new_ppl)
        data.add(new_ppl)

with open('data-big.txt', 'w') as f :
    for el in data : 
        f.write(el + '\n')


def index(L):
    D ={}
    for person in L : 
        first = person['first_name']
        last = person['last_name']
        D[(first, last)] = person 
    return D 


def nb_firstnames(L):
    s=set()
    for person_ in L : 
        s.add(person['first_name'])
    return len(s)