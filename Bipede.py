import random

class Bipede():

    def __init__(self, nom, sexe):
        self.nom = nom
        self.sexe = sexe
        self.caractere = random.choice(["gentil", "méchant"])
    
    def marcher(self, x, y):
        print(f"Je vais me déplacer en (X : {x}, Y : {y}).")

    def __str__(self):
        return (f"{self.nom} ({self.sexe}) et il est {self.caractere}.")

if __name__ == "__main__":
    pass