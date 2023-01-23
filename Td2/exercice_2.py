###TD2

##Exercice 2
f=open("dico.txt",encoding="latin1")
dic = f.read().split("\n")

def reverse(dic):

    dictionnaire = {'i':1,'z':2,'e':3,'h':4,'s':5,'g':6,'l':7,'b':8,'g':6,'d':0,'o':0}
    lst = []
    lst_digit=[]
    for i in dic:
        if set(i) <= set(dictionnaire.keys()):
            lst.append(i)
    for word in lst:
        lst_digit.append("".join([str(dictionnaire[x]) for x in word[::-1]]))
    return lst,lst_digit


def find_word(word,dico):
    for letter in word:
        
        if letter in dico :#and dico[letter]!=0:
            dico[letter]-=1
        else:
            return None
    return word

def reset_dico(string,dico):
    for letter in string:
        dico[letter] = string.count(letter)
    return dico

def lookup(string):
    f=open("dico.txt",encoding="latin1")
    dic = f.read().split("\n")
    dico = {}
    lst=[]
    reset_dico(string,dico)
    for word in dic:
        wd=find_word(word,dico)
        reset_dico(string,dico)
        if None!= wd:
            lst.append(wd)
    return lst
        





        
    return list 

#print(reverse(dic))
print(lookup("XWRDYTRERASZ"))
