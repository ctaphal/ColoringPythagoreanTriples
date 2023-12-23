def ptripleFinder(n):
    # find all Pythagorean triples containing values from 1 to n and store in ptriples (list of lists)
    # (brute force Pythagorean triples finder; includes multiples of simplified Pythagorean triples (ex. 6, 8, 10))
    ptriples = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if ((i**2 + j**2 == k**2) and (i<j)):
                    #i<j condition is to prevent adding duplicate triples from being added to ptriples
                    #(ex. to prevent b^2 + a^2 = c^2 from also being counted as a separate triple)
                    ptriples.append([i,j,k])

    return ptriples
                    

def noTriplesChecker(stA, stB, stC, ptriples):
    #check whether any set has a triple in it; return True if good, return False if any set has a triple

    for triple in ptriples:
        first = triple[0]
        second = triple[1]
        third = triple[2]

        if (first in stA) and (second in stA) and (third in stA):
            print(f"Failing triple ({first},{second},{third}) in Set A")
            return False
        
        if (first in stB) and (second in stB) and (third in stB):
            print(f"Failing triple ({first},{second},{third}) in Set B")
            return False
        
        if (first in stC) and (second in stC) and (third in stC):
            print(f"Failing triple ({first},{second},{third}) in Set C")
            return False
        
    #print("set A:",stA)
    #print("set B:",stB)
    #print("set C:",stC)
    if len(stA.intersection(stB))!=0:
        print(stA.intersection(stB))
        return False
    if len(stB.intersection(stC))!=0:
        print(stB.intersection(stC))
        return False
    if len(stC.intersection(stA))!=0:
        print(stC.intersection(stA))
        return False
    
    return True


def k3Checker(first, second, third, stA, stB, stC, ptriples):
 
    allGood = True
    if (first in stB) or (first in stC):
        return False

    totalSet = (stA.union(stB)).union(stC)
    if (first in totalSet) and (second in totalSet) and (third in totalSet):
        return True

    stA.add(first)

    if ((second in stA) and (third in stA)):
        stA.remove(first)
        return False
    
    added2nd = False
    added3rd = False
    
    if (second in stA):
        if (third not in stC):
            stB.add(third)
            added3rd = True
    allGood = noTriplesChecker(stA, stB, stC, ptriples)
    if (allGood == False):
        if (added3rd==True):
            stB.remove(third)
            added3rd = False

    if (second in stA):
        if (third not in stB):
            stC.add(third)
            added3rd = True
    allGood = noTriplesChecker(stA, stB, stC, ptriples)
    if (allGood == False):
        if (added3rd==True):
            stC.remove(third)
            added3rd = False
    if (third in stA):
        if (second not in stC):
            stB.add(second)
            added2nd = True
    allGood = noTriplesChecker(stA, stB, stC, ptriples)
    if (allGood == False):
        if (added2nd==True):
            stB.remove(second)
            added2nd = False

    if (third in stA):
        if (second not in stB):
            stC.add(second)
            added2nd = True
    allGood = noTriplesChecker(stA, stB, stC, ptriples)
    if (allGood == False):
        if (added2nd==True):
            stC.remove(second)
            added2nd = False

    added2nd = False
    added3rd = False

    if (second not in stA) and (second not in stB) and (second not in stC):
        stB.add(second)
        added2nd = True


    if (third not in stA) and (third not in stB) and (third not in stC):
        stC.add(third)
        added3rd = True

    allGood = noTriplesChecker(stA, stB, stC, ptriples)
    if (allGood == False):
        if (added2nd==True):
            stB.remove(second)
            added2nd = False
        if (added3rd==True):
            stC.remove(third)
            added3rd = False
        if (second not in stB) and (second not in stC):
            stC.add(second)
            added2nd = True
        if (third not in stB) and (third not in stC):
            stB.add(third)
            added3rd = True
    else: 
        return True

    allGood = noTriplesChecker(stA, stB, stC, ptriples)
    if (allGood == False):
        if (added2nd==True):
            stC.remove(second)
            added2nd = False
        if (added3rd==True):
            stB.remove(third)
            added3rd = False
        if (second not in stB) and (second not in stC):
            stC.add(second)
            added2nd = True
        if (third not in stB) and (third not in stC):
            stC.add(third)
            added3rd = True
    else:
        return True
    
    allGood = noTriplesChecker(stA, stB, stC, ptriples)
    if (allGood == False):
        if (added2nd==True):
            stC.remove(second)
        if (added3rd==True):
            stC.remove(third)
        stA.remove(first)
        return False
    else:
        return True


setA = set()
setB = set()
setC = set()

n = int(input("Enter a value for n: "))
ptriples = ptripleFinder(n)

failure = False

for i in range (1, n+1):
    #print("AT n =", i)
    ntriples = []
    for t in ptriples:
        if i in t:
            ntriples.append(t)

    for ntriple in ntriples:
        copy = []
        for num in ntriple:
            copy.append(num)
        copy.remove(i)

        first = i
        second = copy[0]
        third = copy[1]

        doesItWork = k3Checker(first, second, third, setA, setB, setC, ptriples)
        if (doesItWork == False):
            doesItWork = k3Checker(first, second, third, setB, setA, setC, ptriples)
            if (doesItWork == False):
                doesItWork = k3Checker(first, second, third, setC, setA, setB, ptriples)
                if (doesItWork == False):
                    failure = True
                    break
        
    if (failure==True):
        print("Failed at n =",i)
        break

if (failure==False):
    print("Success for n =", n)
#print("A intersect B:", setA.intersection(setB))
#print("B intersect C:", setB.intersection(setC))
#print("A intersect C:", setA.intersection(setC))
#print("Set A:", setA)
#print("Set B:", setB)
#print("Set C", setC)