from Bipede import Bipede

class Robot(Bipede):

    def __init__(self, id, marque):
        self.id = id
        self.marque = marque

    def communiquer(self, parole):
        pass

    def reparer(self, requete):
        pass

    def __str__(self):
        return (f"{self.id}, {self.marque}")

if __name__ == "__main__":
    robot_1 = Robot(id=1, marque="Tesla")
    robot_2 = Robot(id=2, marque="Boston Dynamics")
    print(robot_1)
    print(robot_2)
