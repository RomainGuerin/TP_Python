from Robot import Robot
from Humain import Humain

if __name__ == "__main__":
    robot_1 = Robot(nom="IA", sexe="Binaire", id=1, marque="Tesla")
    robot_2 = Robot(nom="VITE", sexe="Quantique", id=2, marque="Boston Dynamics")
    print(robot_1)
    print(robot_2)
    
    robot_1.marcher(5, 10)

    humain_1 = Humain(nom="Guérin", sexe="Homme", prenom="Romain")
    parole = input(f"Que souhaitez-vous demander à {humain_1.getNom()} > ")
    robot_1.communiquer(parole, humain_1)
    
    robot_1.reparer("Meuble cuisine", humain_1)
