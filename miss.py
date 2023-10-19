tab=[1,2, 3]
sequence = [4, 1, 2, 1, 5, 3, 4, 4, 1, 2, 3]

sequenceTwo = [4, 1, 2, 1, 5, 3, 4, 4, 1, 2, 3]





# retourne la position d'un élement dans la séquence
def positionInSequence(elm):
    try:
        return sequence.index(elm)
    except:
        return -1


# le premier occurence de chaque élement du cache
def cacheElmtOccurence():
    apparition=[]
    for elm in tab:
        position = positionInSequence(elm)
        apparition.append(position)
    return apparition


def eleEjectPosition():
    apparition = cacheElmtOccurence()
    for  elm in apparition:
        if elm == -1:
            return apparition.index(elm)
        
    return apparition.index(max(apparition))


def inCache(value):
    for elemt in tab:
        if elemt == value:
            return True
    return False


def addNewInCache():
    hit= 0
    miss= 0
    for elmt in sequenceTwo:
        print(elmt, tab, sequence)
        if inCache(elmt) :
            hit+=1
        else: 
            miss+=1
            ejectPosition = eleEjectPosition()
            tab[ejectPosition]= elmt
        sequence.pop(0) 
    print(miss, tab)

addNewInCache()