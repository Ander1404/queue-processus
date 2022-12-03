

#create a queue
class File:
    def __init__(self):
        self.valeurs=[]
    def enfiler(self,valeur):
        self.valeurs.append(valeur)
    def defiler(self):
        if self.valeurs:
            return self.valeurs.pop(0)
    def estVide(self):
        return self.valeurs==[]
    def longueur(self):
        return len(self.valeurs)
    def __str__(self):
        ch="\n Etat de la file : \n"
        for x in self.valeurs:
            ch+=str(x) + " "
        return ch


#treatment of processus
taille=eval(input("Entrer le nombre de processus"))
quantum=eval(input("Entrer le quantum"))
File1=File()
File2=File()
File3=File()
File4=File()
File5=File()
priorite=[]
tache=[]
TailleFile=[File1,File2,File3,File4,File5]
long=len(TailleFile)
print(File4.estVide())
for i in range(0,taille):
    v=eval(input("Entrer le temps du processus :"))
    tache.append(v)
    b=eval(input("Entrer la priorite du processu:"))
    priorite.append(b)
print(priorite)

#traitement des taches
for i in range(0,taille):
    if priorite[i]==1:
        File1.enfiler(tache[i])
    elif priorite[i]==2:
        File2.enfiler(tache[i])
    elif priorite[i]==3:
        File3.enfiler(tache[i])
    elif priorite[i]==4:
        File4.enfiler(tache[i])
    else:
        File5.enfiler(tache[i])

File1.enfiler(10)
File1.defiler()

File4.enfiler(0)
File5.enfiler(0)
File3.enfiler(0)
File2.enfiler(0)
print(File5.defiler())
#traitement des processus
for i in range(0,taille):
#Traitement du fil 1
    if File1!=None:
        tmp=(File1.defiler())
        if File1!=File1.estVide():
            while(tmp>=quantum):
                tmp-=quantum
                File1.enfiler(tmp)
            print(tmp)
            if tmp<quantum:
                tmp=0
                File1.enfiler(tmp)

            if tmp==0:
                print("Duree epuisee")
        else:
            print("la liste est vide")

#Traitement du file 2
    if File2 != None:
        tmp2 = (File2.defiler())
        if File2 != File2.estVide():
            while (tmp2 >= quantum):
                tmp2 -= quantum
                File2.enfiler(tmp2)
            if tmp2<quantum:
                tmp2=0
                File1.enfiler(tmp2)
            if tmp == 0:
                print("Duree epuisee")
        else:
                print("la liste est vide")

#Traitement du file 3
    if File3!=None:
        tmp3 = (File3.defiler())
        if File2 != File2.estVide():
            while (tmp3 >= quantum):
                tmp3 -= quantum
                File3.enfiler(tmp3)
            if tmp3<quantum:
                tmp3=0
                File3.enfiler(tmp3)

            if tmp == 0:
                print("Duree epuisee")
    else:
        print(" queue is empty")
#Traitement du file 4
    if File4 != None:
        tmp4 = (File4.defiler())
        if File4 != File4.estVide():
            while (tmp4 >= quantum):
                tmp4 -= quantum
                File4.enfiler(tmp4)
            if tmp4<quantum:
                tmp4=0
                File4.enfiler(tmp4)

            if tmp == 0:
                print("Duree epuisee")
        else:
            print(" queue is empty")

#Traitement du file 5
    if File5 != None:

        if File5 != File5.estVide():
            tmp5 = (File5.defiler())
            if tmp5!=None:
                while (tmp5 >= quantum):
                    tmp5 -= quantum
                    File5.enfiler(tmp5)
                if tmp5<quantum:
                    tmp5=0
                    File1.enfiler(tmp5)

                if tmp5 == 0:
                    print("Temps de processus epuisee")
            else:
                print(" queue 5 is empty")

