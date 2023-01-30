# Humain peut demander ordres, et superviser
from Bipede import Bipede
from Robot import Robot

class Humain(Bipede):
    def __init__(self, prenom, nom, sexe):
        self.prenom = prenom
        super().__init__(nom, sexe)

    def demander_ordres(self, ordre, idRobot):
        print(f"{self.nom} demande à robot n° {idRobot} de faire ({ordre})")
        print("Le robot", idRobot, "est en train de faire", ordre)
        return ordre
    
    def superviser(self, robot):
        print("Le robot est en train de faire", robot.ordre)

    def __str__(self):
        return (f"{self.nom} {self.prenom} ({self.sexe})\n")


if __name__ == "__main__":
    robot1 = Robot(nom="IA", sexe="Binaire", id=1, marque="Tesla")
    print(robot1)
    Humain1 = Humain(prenom="Guérin", nom="Romain", sexe="Homme")
    print(Humain1)
    Humain1.demander_ordres("courir vers X : 1458 et Y : -758", robot1.id)
    print(Humain1)
    