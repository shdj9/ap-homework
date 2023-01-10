def parse(file):
    with open(file) as f : 
        L = []
        for line in f :
           M = line.strip().split(" ")
           L.append({
               'firstname': M[0],
               'lastname': M[1],
               'birthdate': (M[2],M[3],M[4])
            })
    return L

#print(parse('data.txt'))
import random as rd 


with open ("first_names.txt") as first :
    with open ("last_names.txt") as last :
        with open('data-big.txt', 'w') as data :
            F = [line.rstrip('\n') for line in first]
            L = [line.rstrip('\n') for line in last]
            people=set()
            n = len(F)
            m = len(L)
            while len(people)<10000:
                f = rd.randint(0, n-1)
                l = rd.randint(0, m-1)
                if (F[f],L[l]) not in people :
                    people.add((F[f],L[l]))
                    data.write(F[f]+" "+L[l]+" "+str(rd.randint(1,28))+"/"+str(rd.randint(1,12))+"/"+str(rd.randint(2000,2004))+'\n')
        data.close()


def parse2(file):
    with open(file) as f : 
        L = []
        for line in f :
           M = line.strip().split(" ")
           L.append({
               'firstname': M[0],
               'lastname': M[1],
               'birthdate': M[2]
            })
    return L
    
nb = 0
firstnames = set()
for people in parse2('data-big.txt'):  
    if people['firstname'] not in firstnames : 
        nb += 1
        firstnames.add(people['firstname']) 
print(nb) 
    
    









