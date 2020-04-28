def repeatedString(s, n):
    lettera = [x for x in s if x == 'a']
    lengths = [len(s), len(lettera)]
    print(lengths)
    numa = int((n // lengths[0]) * lengths[1])
    print(numa)
    remainder = n % lengths[0]
    
    print(s)
    if lengths[0] != lengths[1]:
        for x in range(remainder):
            if s[x] == 'a':
                numa += 1

    if lengths[0] == lengths[1]: numa = n
    
    return numa

#162401559918

#print(repeatedString('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 534802106762))


def rotleft(a,d):
    for i in range(d):
        fvar = a[0]
        a.remove(a[0])
        a.insert(len(a), fvar)
    return a

def isValid(s):
    uniqueChars = set(s)
    occurances = []
    for value in uniqueChars:
        count = 0
        for i in s:
            if value == i:
                count+=1
        occurances.append(count)
    occurances.sort()
    print(occurances)
    oneVar = occurances[0]
    twoVar = occurances[-1]
    oneVarC = 0
    twoVarC = 0
    for x in occurances:
        if (x != oneVar) and (x != twoVar):
            return 'NO' 
        if x == oneVar:
            oneVarC +=1
        elif x == twoVar:
            twoVarC +=1
    if (twoVarC > 1) or (oneVarC > 1):
        return 'NO'
            
    #print(test)
    occurances = list(set(occurances))
    print(occurances)
    if len(occurances) == 1:
        return 'YES'
    if len(occurances) == 2:
        if ((occurances[0] + 1) == occurances[1]) or ((occurances[0] - 1) == occurances[1]) or (occurances[0] == 1):
            return 'YES'
    else: return 'NO'

print(isValid('aaaaabc'))
