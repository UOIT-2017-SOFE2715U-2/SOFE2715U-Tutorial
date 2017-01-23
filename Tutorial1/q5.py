from abc import ABCMeta, abstractmethod, abstractproperty

# defining abstract class
class Pet(object):
    __metaclass__ = ABCMeta

    name = None
    age = None
    sex = None

    def __init__(self,name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def get_sex(self):
        return self.sex

# abstract functions
    @abstractmethod
    def speak(self):
        pass
    def get_type(self):
        pass

# define classes of type Pet
class Dog(Pet):
    def speak(self):
        return "Bark Bark!"

    def get_type(self):
        return "Dog"

class Cat(Pet):
    def speak(self):
        return "Meow!"

    def get_type(self):
        return "Cat"

# creat objects of type Cat and Dog
myCat = Cat("Toby", 2,"male")
myDog = Dog("Bella", 3, "female")
myPets = [myCat,myDog]

for pet in myPets:
    print "My", pet.get_type(), pet.get_name(), "says", pet.speak()
    print pet.get_name(), "is", pet.get_age(), "years old", pet.get_sex(), ".\n"
