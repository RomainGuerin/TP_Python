from Bipede import Bipede

class Robot(Bipede):

    def __init__(self, nom, sexe, id, marque, tache=""):
        super().__init__(nom, sexe)
        self.id = id
        self.marque = marque
        self.tache = tache

    def communiquer(self, parole, humain):
        print(f"{self.nom} demande à {humain.getNom()} : '{parole}'")

    def reparer(self, requete, humain):
        print(f"{self.nom} répare à la demande de {humain.nom} : '{requete}'")

    def getId(self):
        return self.id

    def getTache(self):
        return self.tache

    def __str__(self):
        return (f"Robot n°{self.id} ({self.sexe})\nNom d'usage : {self.nom}\nFabriqué par : {self.marque}\n")
