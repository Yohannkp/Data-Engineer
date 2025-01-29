import Bibliotheque
import Livre



bb = Bibliotheque.Bibliotheque("Mediatheque")

while True:
    print("GESTION BIBLIOTHEQUE")
    Menu = ["Ajouter un livre","Modifier un livre","Supprimer un livre","Liste livres","Rechercher un livre","Sauvegarder","Exit"]

    print("Menu")
    for i in range(0,len(Menu)):
        print(i+1,Menu[i])
        
    tache = int(input("Que voulez vous faire? : "))
    if tache>=len(Menu)+1:
        print("Choisissez un élément du menu s'il vous plais")
    else:
        if tache == 1 : 
            print("Vous avez selectionné : ",Menu[tache-1])
            nom = input("Entrer le nom du livre : ")
            auteur = input("Entrer l'auteur du livre : ")
            date = input("Entrer la date de publication du livre : ")
            livre = Livre.Livre(nom,auteur,date)
            bb.AjouterLivre(livre)
            print(bb.livres)
            
        elif tache == 2 : 
            for i in range(0, len(bb.livres)):
                print(i+1," : ",bb.livres[i])
            livreid = int(input("Entrer le numero du livre a modifier : "))
            print("1 : Nom du livre , 2  : Auteur du livre , 3 : Date de publication")
            modificationid = int(input("Que voulez vous modifier ? : "))
            if modificationid == 1:
                newnom = input("Entrer le nouveau nom")
                bb.livres[livreid-1].nom = newnom
                    
            elif modificationid == 2:
                newauteur = input("Entrer le nouvel auteur")
                bb.livres[livreid-1].auteur = newauteur
            else:
                newdate = input("Entrer la nouvelle date")
                bb.livres[livreid-1].date = newdate
            print("Apres modification")
            bb.listLivre()
        
        elif tache == 3 : 
            bb.listLivre()
            livreid = int(input("Quelle livre voulez vous supprimer ? "))
            bb.SupprimerLivre(livreid)
            
            
        elif tache == 4 :
            bb.listLivre()
            
        elif tache == 5 :
            recherche = input("Entrer une information sur le livre que vous rechercher")
            bb.RechercheLIvre(recherche)
            
        elif tache == 6:
            bb.sauvegarder_donnees()
            
        
        elif tache == 7:
            print("Exit")
            break
