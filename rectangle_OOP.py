class Rectangle:
                  def __init__(self, length, breadth):
                        self.length = length
                        self.breadth = breadth

                  def area(self):
                         return self.length * self.breadth
               
a = int(input("Enter length of rectangle: "))
b = int(input("Enter breadth of rectangle: "))

obj = Rectangle(a,b)

print(f"Area of Rectangle: {obj.area()}")

print()




                