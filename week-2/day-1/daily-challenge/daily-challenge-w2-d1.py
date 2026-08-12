class Farm():
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count=1):
        if animal_type not in self.animals:
            self.animals[animal_type] = count
        else:
            self.animals[animal_type] += count

    def get_info(self):
        result = ""
        for key, value in self.animals.items():
            result = result + f"{key}: {value}\n"
        return f"{self.name}\n" + f"{result}" + f"E-I-E-I-O"


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.add_animal('goat')
print(macdonald.get_info())
