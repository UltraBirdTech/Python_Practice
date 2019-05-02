class Person():
   def __init__(self, name):
       self.name = name

   def introduction(self):
       print("My name is '" + self.name + "'")

someone = Person('steeve')
print(someone.name)
someone.introduction()
