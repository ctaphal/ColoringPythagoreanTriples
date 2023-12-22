# find all Pythagorean triples containing values from 1 to n and store in ptriples (list of lists)
def ptripleFinder(n):
    #brute force Pythagorean triples finder
    ptriples = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if ((i**2 + j**2 == k**2) and (i<j)):
                    #i<j condition is to prevent adding duplicate triples from being added to ptriples
                    #(ex. to prevent b^2 + a^2 = c^2 from also being counted as a separate triple)
                    ptriples.append([i,j,k])

    return ptriples
                    

def noTriplesChecker(stA, stB, stC):
    #check whether any set has a triple in it; return True if good, return False if any set has a triple


def k3Checker(num1, num2, num3, stA, stB, stC):

    allGood = True

    stA.add(first)
    if ((second in stA) and (third in stA)):
        return False
    elif (second in stB):
        if (third not in stC):
            stC.add(third)
            if (allGood = False)

    # put n in A, then remove n from triple; if other two number

    return False


setA = set()
setB = set()
setC = set()

n = 20
ptriples = ptripleFinder(n)

for i in range (1, n+1):

    ntriples = []
    for t in ptriples:
        if i in t:
            ntriples.append(t)

    failure = FALSE
    for ntriple in ntriples:
        ntriple.remove(i)

        first = i
        second = ntriple[0]
        third = ntriple[1]

        doesItWork = k3Checker(first, second, third, setA, setB, setC)
        if (doesItWork == False):
            failure = True
            print("Fails")
            break
    
    if (failure == True):
        break