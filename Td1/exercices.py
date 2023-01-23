""" Exercice 1 """
def circle_char(message):
    print( "*"*(len(message)+4)+"\n* "+message+" *\n"+"*"*(len(message)+4) if len(message) <75 else "")


""" Exercice 2 """
def circle_char_dot(message):
    print("*"*79+"\n*"+'.'*((79 - len(message))//2 -1)+message+'.'*((79 - len(message))//2 -1)+"*\n"+"*"*79 if len(message) < 79 else "")

""" Exercice 3 """
def find_message(message):
    print(message[(len(message)//3 +3):-(len(message)//3 +3)])

""" Exercice 4 """
def tricote(s1,s2):
    print("".join([s1[i]+s2[i] for i in range (min(len(s1),len(s2)))])+s1[min(len(s1),len(s2)):]+s2[min(len(s1),len(s2)):])

""" Exercice 5 """
def detricote(msg):
    #print("".join([msg[i] for i in range(len(msg)) if i%2==0]),"".join([msg[i] for i in range(len(msg)) if i%2!=0]))
    print(msg[::2]+" " +msg[1::2] )

char = "coin coin"
circle_char(char)
circle_char_dot(char)

char2 ="*"*13+"\n* coin coin *\n"+"*"*13
find_message(char2)

s1="abcdef"
s2="0123456789"
tricote(s1,s2)

msgs1s2= "a0b1c2d3e4f56789"
detricote(msgs1s2)


daltons=[{"nom":"joe","taille":140,"caractere":"teigneux"},
{"nom":"jack","taille":155,"caractere":"idiot"},
{"nom":"william","taille":170,"caractere":"stupide"},
{"nom":"averell","taille":185,"caractere":"abruti"}]

#print("\n")
#print (daltons)
#daltons.sort(key=lambda x:x['nom'])
#print("\n")
#print (daltons)
#daltons.sort(key=lambda x:x['taille'])
#print("\n")
#print (daltons)
