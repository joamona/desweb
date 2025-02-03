class Bird:
    species = "Bird"  # This is a class variable shared by all instances.
    def __init__(self, name):
        self.name = name  # This is an instance variable, unique to each instance.

bird1 = Bird("Parrot")
bird2 = Bird("Sparrow")

#print the class variable inboth instances
print(bird1.species)  # Output: Bird
print(bird2.species)  # Output: Bird

# Change the class variable
bird1.species = "dog" # <--NEW INSTANCE VARIABLE WITH THE SAME NAME
#the class variable is changed for al the Bird instances
print(bird1.species)   # Output: dog
print(bird2.species)   # Output: Bird

Bird.species = "Fish"
print(bird1.species)   # Output: dog  # <--The instance variable is returned. The class variable is not accessible any more
print(bird2.species)   # Output: Bird