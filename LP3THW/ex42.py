## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):

	def __init__(self, name):
		## Dog has-a name of some kind
		self.name = name # name = Animal

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name of some kind
		self.name = name # name = Animal

## Person is-a object
class Person(object):

	def __init__(self, name):
		## Person has-a name of some kind
		self.name = name # name = ?

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employeee(Person):

	def __init__(self, name, salary):
		## Subclass employee has-a salary
		super(Employee, self).__init__(name) # super() is a way to define subclass / https://www.pythonforbeginners.com/super/working-python-super-function
		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish
class Halibut(Fish):
	pass

## rover is-a Dog => "Set rover to instance of Dog() = "Rover"
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet is-a satan 
mary.pet = satan

## frank is-a Employee ??
frank = Employee("Frank",120000)

## frank has-a pet is-a rover
frank.pet = rover

## flipper is an instance of Fish()
flipper = Fish()

## crouse is an instance of Salmon()
crouse = Salmon()

## harry is an instance of Halibut()
harry = Halibut()