class Plant:
    def __init__(self, type, size, is_blooming=False):
        self.type = type
        self.size = size
        self.is_blooming = is_blooming

    def grow(self):
        self.stop_blooming()
        if (self.size) == "small":
            (self.size) == "medium"
        else:
            (self.size) == "large"

    def bloom(self):
        self.is_blooming = True

    def stop_blooming(self):
        self.is_blooming = False

    def status(self):
        print(
            f"Type: {self.type}, size : {self.size}, is_blooming: {self.is_blooming}")


my_plants = [Plant("rose", "small"), Plant("sunflower", "medium"),
             Plant("tulip", "small"), Plant("cactus", "large", True), Plant("orchid", "medium", True)]

for plant in my_plants:
    plant.grow()
    plant.status()

my_plants[0].bloom()
