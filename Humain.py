# Humain peut demander ordres, et superviser
from Bipede import bipede

class humain():
    def __init__(self, prenom):
        self.prenom = prenom

    def demander_ordres(self, ordre, robot):
        ordre = input("Que voulez-vous faire? ")
        return ordre
    
    def superviser(self, robot):
        print("Le robot est en train de faire", robot.ordre)


if __name__ == "__main__":
    humain = humain("Romain", "Guérin")
    humain_2 = humain("LE HUEROU", "Corentin")
