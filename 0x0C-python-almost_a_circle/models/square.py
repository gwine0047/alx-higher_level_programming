"""This module defines a Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defining the square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Rectangle class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overriding the __str__ method"""

        return (
            f"[Square] ({self.id}) "
            f"{self.x}/{self.y} - "
            f"{self.width}")

    @property
    def size(self):
        """getting the size"""
        return self.width

    @size.setter
    def size(self, value):
        """setting value for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns argument to attributes based on position"""
        if args:
            for num, value in enumerate(args):
                if num == 0:
                    self.id = value
                elif num == 1:
                    self.size = value
                elif num == 2:
                    self.x = value
                elif num == 3:
                    self.y = value
                else:
                    break
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "size":
                    self.width = value
                    self.height = value
                # elif key == "height":
                #     self.size == value
                elif key == "id":
                    self.id = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    break

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        sqr_dic = {
            "id":self.id,
            "x":self.x,
            "size":self.width,
            "y":self.y
        }
        return sqr_dic
