import json
import Livre


class Bibliotheque:
    def __init__(self,nom,fichier_json = "Bibliotheque.json"):
        self.nom = nom
        self.livres = [Livre.Livre("Aya de yopougon","Yohann", "16 janvier 2026")]
        self._fichier_json = fichier_json
        
    def AjouterLivre(self,livre):
        self.livres.append(livre)
        
    def listLivre(self):
        for i in range(0, len(self.livres)):
            print(i+1,self.livres[i])
            
    def SupprimerLivre(self,livreid):
        self.livres.pop(livreid-1)
        
    def RechercheLIvre(self,recherche):
        for i in self.livres:
            if recherche in i.nom:
                print("Trouvé : ",i)
                break
            elif recherche in i.auteur:
                print("Trouvé", i)
                break
            elif recherche in i.date:
                print("Trouvé : ",i)
                break
    # Charger les livres depuis le fichier JSON
    def charger_donnees(self):
        try:
            with open(self._fichier_json, "r", encoding="utf-8") as fichier:
                data = json.load(fichier)
                return [Livre.Livre.from_dict(livre) for livre in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Retourne une liste vide si le fichier n'existe pas ou est corrompu

        
    # Sauvegarder les données dans un fichier JSON
    def sauvegarder_donnees(self):
        with open(self._fichier_json, "w", encoding="utf-8") as fichier:
            json.dump([livre.to_dict() for livre in self.livres], fichier, indent=4)
        print("Ouverture")
        
        
    @property
    def fichier_json(self):
        return self._fichier_json

    @fichier_json.setter
    def fichier_json(self, valeur):
        self._fichier_json = valeur
        

