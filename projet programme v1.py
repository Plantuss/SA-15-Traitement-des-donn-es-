import csv
import datetime
from tkinter import * 
from tkcalendar import * 

groupe_possible = ["TDFourier", "TDBell","RT1Turing", "RT1Huffman", "RT1App", "RT1-S1", "RT1Shannon1", "RT1Shannon2", "RT2Dijkstra","RT2Hamming","RT2App","LP-CyberSÃ©curitÃ©","LP-GSIE-ARE-1","RT2-S3"]
groupe1 = input("Donner le groupe TD(ex :TDFourier, TDBell, RT2Hamming..) :")

while groupe1 not in groupe_possible: 
    print("Ce groupe n'existe pas : ")
    groupe1 = input("Donner le groupe TD(ex :TDFourier, TDBell, RT2Hamming..) :")

groupe = []
groupe.append(groupe1)

#On a maintenant le groupe qu'il faut chercher de manière sécurisé car on ne peut pas mettre un groupe inexistant

table=[]
with open("test.csv",newline="") as csvfile:
    reader=csv.reader(csvfile,delimiter=",")
    for row in reader:
        table.append(row)



rentrée1 = ["2021-09-01"]
rentrée2 = ["2021-11-08"]
rentrée3 = ["2022-01-03"]

matieres1 = []
matieres2 = []
matieres3 = []

for i in table:
    a = i[2]

    if a[0:10] in rentrée1:
        matieres1.append(i)
    elif a[0:10] in rentrée2:
        matieres2.append(i)
    elif a[0:10] in rentrée3:
        matieres3.append(i)

#on se retrouve avec 3 listes avec uniquement les matières des jours de rentré

for i in matieres1[:]: 
    a = i[3]
    position = a.find(groupe[0])

    if position != -1:
        continue
    else:
        matieres1.remove(i)

jour_rentree = 1
mois = "2021-09-0"
compter = 9

while len(matieres1) == 0: 
    
    rentrée1 = [mois + str(jour_rentree)]

    for i in table:
        a = i[2]

        if a[0:10] in rentrée1:
            matieres1.append(i)
    for i in matieres1[:]: 
        a = i[3]
        position = a.find(groupe[0])

        if position != -1:
            continue
        else:
            matieres1.remove(i)
        
    jour_rentree = jour_rentree + 1

    if jour_rentree > 31:
        mois = "2021-" + str(compter+1) + "-0"
        compter +=1
        jour_rentree = 1
        if compter >= 12: 
            compter = 0

for p in matieres2[:]: 
    a = p[3]
    
    position = a.find(groupe[0])

    if position != -1:
        continue
    else:
        matieres2.remove(p)

for b in matieres3[:]: 
    a = b[3]
    position = a.find(groupe[0])

    if position != -1:
        continue
    else:
        matieres3.remove(b)

# On se retrouve avec des listes de matière uniquement avec le groupe voulu pour les 3 rentrées
#Il reste à savoir l'heure la plus tôt pour chaque jour pour afficher les informations de la première heure de cours. 
        
print("Pour la première rentrée\n")

min = datetime.datetime(2024,12,31,23,59,59)
matiere1_fin = []
for k in matieres1:

    année = int(k[1][0:4])
    mois = int(k[1][5:7])
    jour = int(k[1][9:10])
    heure = int(k[1][11:13])
    minutes = int(k[1][14:16]) 

    time = datetime.datetime(année,mois,jour,heure,minutes)

    if time < min :
        min = time
        matiere1_fin.clear()
        matiere1_fin.append(k)
    
for w in matiere1_fin: 
    année = int(w[1][0:4])
    mois = int(w[1][5:7])
    jour = int(w[1][9:10])
    heure = int(w[1][11:13])
    minutes = int(w[1][14:16])


for valeur in matiere1_fin: 
    salle = valeur[4]
    heure_fin = int(valeur[2][11:13])
    minutes_fin = int(valeur[2][14:16])
    day_num = datetime.date(année,mois,jour).weekday()
    prof = valeur[3]
    matiere = valeur[0]

week_day = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi", "Samedi", "Dimanche"]
print(week_day[day_num], rentrée1,"de",heure,":", minutes," à ", heure_fin,":",minutes_fin, "dans la salle ", salle, "avec ", prof, "en", matiere,"\n")

window = Tk()
window.geometry("600x600")
window.title("rentrée 1")

Cal = Calendar(window, selectmode = "day", year = année, month = mois, day = jour )
Cal.pack(pady = 20)

information = Label(window, text = (week_day[day_num], rentrée1,"de",heure,":", minutes," à ", heure_fin,":",minutes_fin, "dans la salle ", salle, "avec ", prof, "en", matiere,"\n"))
information.pack(pady = 50)

print("Pour la deuxieme rentrée\n")

min = datetime.datetime(2024,12,31,23,59,59)
matiere2_fin = []

for o in matieres2:
    année = int(o[1][0:4])
    mois = int(o[1][5:7])
    jour = int(o[1][9:10])
    heure = int(o[1][11:13])
    minutes = int(o[1][14:16])

    time = datetime.datetime(année,mois,jour,heure,minutes)
    
    if time < min : 
        min = time
        matiere2_fin.clear()
        matiere2_fin.append(o)


for p in matiere2_fin: 
    année = int(p[1][0:4])
    mois = int(p[1][5:7])
    jour = int(p[1][9:10])
    heure = int(p[1][11:13])
    minutes = int(p[1][14:16])
    

for valeur1 in matiere2_fin:
    salle = valeur1[4]
    heure_fin = int(valeur1[2][11:13])
    minutes_fin = int(valeur1[2][14:16])
    day_num = datetime.date(année,mois,jour).weekday()
    prof = valeur1[3]
    matiere = valeur1[0]

week_day = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi", "Samedi", "Dimanche"]

if rentrée1 != rentrée2:
    print(week_day[day_num], rentrée2,"de",heure,":", minutes," à ", heure_fin,":",minutes_fin, "dans la salle ", salle, "avec ", prof, "en", matiere, "\n")

print("Pour la troisième rentrée")

min = datetime.datetime(2024,12,31,23,59,59)
matiere3_fin = []

for v in matieres3:
    année_r3 = int(v[1][0:4])
    mois_r3 = int(v[1][5:7])
    jour_r3 = int(v[1][9:10])
    heure_r3 = int(v[1][11:13])
    minutes_r3 = int(v[1][14:16])

    time = datetime.datetime(année_r3,mois_r3,jour_r3,heure_r3,minutes_r3)
    
    if time < min : 
        min = time
        matiere3_fin.clear()
        matiere3_fin.append(v)

for t in matiere3_fin: 
    année_r3 = int(t[1][0:4])
    mois_r3 = int(t[1][5:7])
    jour_r3 = int(t[1][9:10])
    heure_r3 = int(t[1][11:13])
    minutes_r3 = int(t[1][14:16])

for valeur2 in matiere3_fin:
    salle_r3 = valeur2[4]
    heure_fin_r3 = int(valeur2[2][11:13])
    minutes_fin_r3 = int(valeur2[2][14:16])
    day_num = datetime.date(année,mois,jour).weekday()
    prof_r3 = valeur2[3]
    matiere_r3 = valeur2[0]

week_day = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi", "Samedi", "Dimanche"]

if rentrée1 != rentrée3:
    print(week_day[day_num], rentrée3,"de",heure_r3,":", minutes_r3," à ", heure_fin_r3,":",minutes_fin_r3, "dans la salle ", salle_r3, "avec ", prof_r3, "en", matiere_r3, "\n")

def Cal2():
    window.quit()
    windows2 = Tk()
    windows2.geometry("600x600")
    windows2.title("rentrée 2") 

    Cal =  Calendar(windows2, selectmode = "day", year = année, month = mois, day = jour )
    Cal.pack(pady = 20)
    informations = Label(windows2, text = (week_day[day_num], rentrée2,"de",heure,":", minutes," à ", heure_fin,":",minutes_fin, "dans la salle ", salle, "avec ", prof, "en", matiere,"\n"))
    informations.pack(pady = 50)

    def Cal3(): 
        windows2.quit()
        windows3 = Tk()
        windows3.geometry("600x600")
        windows3.title("rentre 3")

        Cal3 = Calendar(windows3, selectmode = "day", year = année_r3, month = mois_r3, day = jour_r3)
        Cal3.pack(pady = 50)
        informations = Label(windows3, text = (week_day[day_num], rentrée3,"de",heure_r3,":", minutes_r3," à ", heure_fin_r3,":",minutes_fin_r3, "dans la salle ", salle_r3, "avec ", prof_r3, "en", matiere_r3,"\n"))
        informations.pack(pady = 50)
        windows3.mainloop()
     
    rt_suivante = Button(windows2, text = "rentrée suivante", command = Cal3) 
    rt_suivante.pack(pady = 80)

    windows2.mainloop()

rt_suivante = Button(window, text = "rentrée suivante", command = Cal2) 
rt_suivante.pack(pady = 80)

window.mainloop()