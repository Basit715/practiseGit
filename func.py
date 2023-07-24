class Person:
     def __init__(self, name, age):
          self.name = name
          self.age = age
          
     def show(self):
          print(f"The name is {self.name}")
          print(f"The age is {self.age}")
          
     def showTogether(self):
          print(f"The name is {self.name} and the age is {self.age}")
          
          
p = Person("Basit", 25)
p.show() 