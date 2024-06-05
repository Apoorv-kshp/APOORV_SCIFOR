"""
What is Polymorphism: The word polymorphism means having many forms. 
In programming, polymorphism means the same function name (but different signatures) being used for different types. 
The key difference is the data types and number of arguments used in function.

"""

class Bird:
def intro(self):
	print("There are many types of birds.")
	
def flight(self):
	print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
def flight(self):
	print("Sparrows can fly.")
	
class ostrich(Bird):
def flight(self):
	print("Ostriches cannot fly.")
	
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()



Output

There are many types of birds.
Most of the birds can fly but some cannot.
There are many types of birds.
Sparrows can fly.
There are many types of birds.
Ostriches cannot fly.



