from Bipede import Bipede

class Robot(Bipede):

    def __init__(self, nom, sexe, id, marque):
        super().__init__(nom, sexe)
        self.id = id
        self.marque = marque

    def communiquer(self, parole):
        pass

    def reparer(self, requete):
        pass

    def __str__(self):
        return (f"Robot n°{self.id} ({self.sexe})\nNom d'usage : {self.nom}\nFabriqué par : {self.marque}\n")

if __name__ == "__main__":
    robot_1 = Robot(nom="IA", sexe="Binaire", id=1, marque="Tesla")
    robot_2 = Robot(nom="VITE", sexe="Quantique", id=2, marque="Boston Dynamics")
    print(robot_1)
    print(robot_2)
