import copy

def main():
    point1 = Point(2, 3)
    point2 = copy.deepcopy(point1)

    print("x", point1.x, point1.y)
    print("y", point1.x, point2.y)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == "__main__":
    main()
        
