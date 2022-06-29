
prof=input("veuillez entrer le nom du prof ? \t: ")
nom=input("veuillez entrer votre nom ? \t: ")
age=input("veuillez entrer votre age ?\t: ")
print("Bonjour {}, tu as  {} ans, mr {} est venu il est déjà en classe ".format(nom,age,prof))

Nom= input("veuillez saisir votre nom : ")
Age= int (input("veuillez saisir votre age : "))
print ("Bonjour ",Nom,",tu as ",Age,"ans et bienvenu à l'université")
print("Bonjour {}, tu as {} ans et bienvenue à l'université ".format(Nom,Age))


largeur= float(input("veiullez entrr la largeur du rectangle :"))
longeur= float(input("veiullez entrr la longeur du rectangle :"))
s=longeur*largeur
p=(longeur+largeur)*2
print("la surface du rectangle est :",format(s,".2f"))
print("le perimétre  du rectangle est :",format(p,".2f"))

X= float(input("veuillez saisir la valeur de X :"))
Y= float(input("veuillez saisir la valeur de Y :"))
p=X ** Y
print("la puissance est :",p)

A=float(input("veuillez la valeur de A :"))
B=float(input("veuillez la valeur de B :"))
S= A + B
P= A * B
Df= A - B
Dv= A / B
print("A + B :",format(S, ".2f"))
print("A * B :",format(P, ".2f"))
print("A - B :",format(Df, ".2f"))
print("A / B :",format(Dv, ".2f"))


N1= float(input(" veuillez entrer votre note N1 :"))
N2= float(input(" veuillez entrer votre note N2 :"))
N3= float(input(" veuillez entrer votre note N3:"))
N4= float(input(" veuillez entrer votre note N4:"))
N5= float(input(" veuillez entrer votre note N5 :"))
S= N1 + N2 + N3 + N4 + N5 
M= S/5
print("la somme des notes est :",S)
print("la moyenne des notes est :",format(M,".2f"))

import math
R=float(input("veuillez saisir le rayon du sphére :"))
V= (4 *math.pi * (R**3))/3
print("le volume du sphére est :",format(V,".2f"))

A=int(input("veuillez saisir la valeur de A:"))
B=int(input("veuillez saisir la valeur de B:"))
#C= A
#A= B
#B= C
A,B=B,A
print("la nouvelle valeur de A est : ",A)
print("la nouvelle valeur de B est : ",B)

T=int(input("veuillez saisir la durée en seconde : ")) #
H= T // 3600
R= T % 3600
M= R // 60
S= R % 60
print(H, "H:",M,"m:",S,"s")

import math
Xa=float(input("veuillez saisir la coordonnée X de A :")) #
Ya=float(input("veuillez saisir la coordonnée Y de B :"))
Xb=float(input("veuillez saisir la coordonnée X de A :"))
Yb=float(input("veuillez saisir la coordonnée Y de B :"))
AB = (Xb-Xa)** 2 + (Yb-Ya)**2
AB= math.sqrt(AB)
print("la distance entre les deux pints A et B est :",format(AB, ".2f"))


R1 = float(input("veuillez saisir la valeur de R1 : ")) #
R2 = float(input("veuillez saisir la valeur de R2 : "))
R3 = float(input("veuillez saisir la valeur de 31 : "))
Rser = R1 + R2 + R3
Rpar = (R1*R2*R3)/(R1*R2+R1+R3+R3*R2)
print("la valeur de la résistance en série est :",format(Rser,".2f"))
print("la valeur de la résistance en parallèle est :",format(Rpar,".2f"))

A=int(input("veuillez saisir la valeur de A : "))
B=int(input("veuillez saisir la valeur de B : "))
if A*B>0 :
    print("Aet B ont le même signe ")
else :
    print(" A et  B  ont deux signes differents")


A=int(input("veuillez saisir la valeur de A :"))
B=int(input("veuillez saisir la valeur de B :"))
if A*B >0 :
    A,B=B,A
else :
    C= A + B
    D= A * B
    A=C
    B=D
print("la nouvelle valeur de A est : ",A)
print("la nouvelle valeur de B est : ",B)

N=int(input("veuillez saisir le nombre des copies :"))
if N < 10 :
    F=N * 0.3
elif N < 30 :
    F= 10 * 0.3 + (N-10) * 0.2
else :
    F=10 * 0.3 + 0.25 +(N-30)*0.2
print("le montant de facture à payer est :",F ,"$")

age= int(input("veuillez entrer l'age de l'enfant  :"))
if age >= 6 and age <= 7 :
    print( "la catégorie de l'enfant est POUSSIN")
elif age >= 8 and age <= 9 :
    print( "la catégorie de l'enfant est PUPILLE")
if age >= 10 and age <= 11 :
    print( "la catégorie de l'enfant est MINIME")
elif age >= 12 and age <= 16:
    print( "la catégorie de l'enfant est CADET")
else :
    print("la categorie n'existe pas ")

N1=float(input("veuillez saisir la premiere N1 :"))
N2=float(input("veuillez saisir la premiere N2 :"))
N3=float(input("veuillez saisir la premiere N3 :"))
Moyenne=(N1+N2+N3)/3
print("la moyenne de l'étudiant est :",format(Moyenne,".2f"))
if Moyenne < 10 :
    print("la mention de l'étudiant est : Insuffissant")
elif Moyenne >= 10 and Moyenne < 12 :
    print(" la mention de l'étudiant est :Passable")
elif Moyenne >= 12 and Moyenne < 14:
    print(" la mention de l'étudiant est :Assez bien")
elif Moyenne >= 14 and Moyenne < 16:
    print(" la mention de l'étudiant est :Bien")
else :
    print("la mention de l'étudiant est :Très bien")

import math
a=float(input("veuillez entrer la valeur de a :"))
b=float(input("veuillez entrer la valeur de b :"))
c=float(input("veuillez entrer la valeur de c :"))
delta= b ** 2 - 4 * a *c
if delta< 0 :
    print("pas de solutions réelless")
elif delta == 0 :
        x= (-b)/(2*a)
        print("la solution est :",x)
else :
    x1= (-b-math.sqrt(delta))/(2*a)
    x2= (-b+math.sqrt(delta))/(2*a)
    print("les solutions sont :",format(x1,".2f"),"et",format(x2,".2f"))


sexe= input("veuillez entrer le sexe de l'habitant (H/F) :")
age=int(input("veuillez entrer l'age de l'habitant :")) 
if ((sexe=="H" and age >= 20) or (sexe=="F" and age >= 18 and age<=35)):
   print("l'habitant est imposable")
else :
    print("l'habitant est non imposable")

PHT= float(input("veuillez saisir le prix hors taxe de produit : "))
Cat=input("veuillez saisir la catégorie de produit :")
if Cat == "A" :
    print("le prix TTC de produit est :",PHT+PHT*0.07) 
elif Cat == "B" :
        print("le prix TTC de produit est :", PHT+PHT*0.02)
elif Cat == "C" :
        print("le prix TTC de produit est :",PHT+PHT*0.25) 
else :
    print("la catégorie n'existe pas ")


 A= float(input("veuillez saisir la valeur de A :"))
 B= float(input("veuillez saisir la valeur de B :"))
 op= input("veuillez saisir l'operateur :")
 if op == "+" :
    print("A + B ",A+B)
elif op == "-" :
    print("A - B ",A-B)
elif op == "/"
     if B != 0 :
        print("A / B =",A/B)
     else :
        print("la division par 0 est impossible")
    elif op== "*" :
        print("A * B =",A*B)
    else :
        print("l'operateur est incorrect")


