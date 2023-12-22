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

        #print(first,second,third)

        if (first in stA) and (second in stA) and (third in stA):
            return False
        
        if (first in stB) and (second in stB) and (third in stB):
            return False
        
        if (first in stC) and (second in stC) and (third in stC):
            return False
        
    return True


def k3Checker(num1, num2, num3, stA, stB, stC, ptriples):

    #not sure if this function is doing what I want it to do

    allGood = True

    if (num1 in stB) or (num1 in stC):
        return False
    
    stA.add(num1)

    if ((second in stA) and (third in stA)):
        return False
    
    if (second not in stB) and (second not in stC):
        stB.add(second)

    if (third not in stB) and (third not in stC):
        stC.add(third)

    allGood = noTriplesChecker(stA, stB, stC, ptriples)
    if (allGood == False):
        if (second not in stB) and (second not in stC):
            stC.add(second)

        if (third not in stB) and (third not in stC):
            stB.add(third)
    else: 
        return True

    allGood = noTriplesChecker(stA, stB, stC, ptriples)
    if (allGood == False):
        if (second not in stB) and (second not in stC):
            stC.add(second)

        if (third not in stB) and (third not in stC):
            stC.add(third)
    else:
        return True
    
    allGood = noTriplesChecker(stA, stB, stC, ptriples)
    if (allGood == False):
        return False
    else:
        return True


setA = set()
setB = set()
setC = set()

n = 300
ptriples = ptripleFinder(n)

failure = False

for i in range (1, n+1):

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
            print("Failed")
            break

print("Success for n =", n)
print("SetA:", setA)
print("SetB:", setB)
print("SetC:", setC)