
class Bird:
    def __init__(self, name, species):
        self.name = name  
        self.species = species  
    
    def fly(self):
        print(f"{self.name} is flying!")
    
    def sing(self):
        print(f"{self.name} is singing!")

class Sparrow(Bird):
    def __init__(self, name, species, color):
        
        super().__init__(name, species)
        self.color = color  
    
    def chirp(self):
        print(f"{self.name} is chirping!")
    
    def display(self):
        print(f"{self.name} is a {self.color} {self.species}.")

sparrow = Sparrow("Jack", "Sparrow", "brown")

sparrow.fly()    
sparrow.sing()   
sparrow.chirp()   
sparrow.display() 

