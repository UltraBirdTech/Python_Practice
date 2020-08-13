from parent import Parent
from child_first_module import ChildModule1 as child_module

class ChildFirst(Parent):
    def __init__(self):
        self.child_module = child_module()
        print("I am Child First Class")
