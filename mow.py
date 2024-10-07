f = open('mow.txt','r')
data = f.read()
f.close()

mow ={}
isWord=False

for c in data:
    if 96 < ord(c.lower()) < 123:
        if not isWord:
            isWord = True
            word = c.lower()
        else:
            word += c.lower()
        #end if
    else:
        if isWord:
            isWord = False
            if word in mow:
                mow[word] += 1
            else:
                mow[word] = 1  
            #end if
        #end if
    #end if
#next c
print(mow)
findWord = input('Enter word to find out how many times it occurs:').lower()

if findWord in mow:
    print(mow[findWord])
else:
    print('Word not recognised')
#end if

print("The size of the dictionary is:",len(mow))

print('meadow' in mow)
print('Five occurs',mow['five'],'times')

del(mow['men'])
print(mow)

def deleteFromDict(item,dict):
    if item in dict:
        del(dict[item])
        return True
    #end if
    return False
#end function

repeat = True
while repeat:
    delWord = input('Enter word to delete:').lower()
    if deleteFromDict(delWord,mow):
        print(mow)
    else:
        print('Word not found')
    #end if
    if input('Try again [y/n]').lower() != 'y':
        repeat = False
    #end if
#until != y
