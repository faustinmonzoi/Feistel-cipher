
N=input("Saisir bloc de taille 8 bits")
BIT=list(N)
FACT=input("Veuillez saisir PI la clé de permutation \n")
pi=list(FACT)


keys=[eval(i) for i in BIT]
permutation=[eval(j) for j in pi]


kwargs=[]
for i in range(0,8):
    a=permutation[i]
    kwargs.append(keys[a])
k1=kwargs[0:4]
k2=kwargs[4:8]



def ou_fiestel(t1,t2):
    tab=[]
    decallage=[]
    for j in range(0,4):
        tab.append(t1[j]^t2[j])
        
    decallage.append(tab[2])
    decallage.append(tab[3])
    decallage.append(tab[0])
    decallage.append(tab[1])
    return decallage


def et_fiestel(t1,t2):
    tab=[]
    decallaged=[]
    for j in range(0,4):
        tab.append(t1[j]&t2[j])
    decallaged.append(tab[3])
    decallaged.append(tab[0])
    decallaged.append(tab[1])
    decallaged.append(tab[2])
    return decallaged

def cipher(t1,t2):
    N=input("Veuillez entrer un bloc de taille 8 bits \n")
    bloc=list(N)
    permutation=input("Veuillez saisir PI la clé de permutation \n")
    pi=list(permutation)
    key=[eval(i) for i in bloc]
    PERMUTATION=[eval(j) for j in pi]
    kwargs=[]
    for i in range(0,8):
        a=PERMUTATION[i]
        kwargs.append(key[a])
    go=kwargs[0:4]
    do=kwargs[4:8]

    d1=[]
    for j in range(0,4):
        d1.append(go[j]^ou_fiestel(t1, t2)[j])

    g1=[]
    for j in range(0,4):
        g1.append(do[j]^(do[j]|ou_fiestel(t1, t2)[j]))

    d2=[]
    for j in range(0,4):
        d2.append(g1[j]^et_fiestel(t1,t2)[j])
    g2=[]
    for j in range(0,4):
        g2.append(d2[j]^(do[j]|ou_fiestel(t1, t2)[j]))
    return d1




print("LES CLES SONT \n")
print(ou_fiestel(k1, k2))
print(et_fiestel(k1, k2))
print(cipher(k1, k2))