class Livre:
    def __init__(self,nom,auteur,date):
        self.nom = nom
        self.auteur = auteur
        self.date = date
        
    def __str__(self):
        return f"Nom du livre : {self.nom} , auteur : {self.auteur} et date de publication : {self.date}"
    
    
    def to_dict(self):
        return {
            "nom": self.nom,
            "auteur": self.auteur,
            "date": self.date
        }
    # Créer un objet Livre à partir d'un dictionnaire JSON
    @staticmethod
    def from_dict(data):
        return Livre(data["nom"], data["auteur"], data["date"])
        # Getter et Setter pour le nom
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, valeur):
        if isinstance(valeur, str) and valeur.strip():
            self._nom = valeur
        else:
            raise ValueError("Le nom du livre doit être une chaîne de caractères non vide.")

    # Getter et Setter pour l'auteur
    @property
    def auteur(self):
        return self._auteur

    @auteur.setter
    def auteur(self, valeur):
        if isinstance(valeur, str) and valeur.strip():
            self._auteur = valeur
        else:
            raise ValueError("Le nom de l'auteur doit être une chaîne de caractères non vide.")

    # Getter et Setter pour la date
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, valeur):
        if isinstance(valeur, str) and valeur.strip():  # On pourrait utiliser datetime pour une validation plus stricte
            self._date = valeur
        else:
            raise ValueError("La date doit être une chaîne de caractères non vide.")
    
    