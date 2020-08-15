from parent import Parent
from child_second_module import ChildModule2 as child_module

class ChildSecond(Parent):
    def __init__(self):
        self.child_module = child_module()
        print("I am Child Second Class")

#    def parent_method(self):
#        child_module().say()
