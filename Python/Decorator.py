# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
            #  benefit: Add additional logic when read, write, or delete attributes
            #  Gives you getter, setter, and deleter method


class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self.__height:.1f}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater zero")

    @width.deleter
    def width(self):
        del self._width

rectangle = Rectangle(3, 4)

# rectangle.width = 2
# rectangle.height = -1

del rectangle.width
# del

# print(rectangle._width)
# print(rectangle._height)