class Base:
    __nb_objects = 0  # Private class attribute to store the number of objects created

    def __init__(self, id=None):
        """
        This is the constructor for the Base class.

        Args:
            id (int, optional): An optional ID to assign to the object.
        """
        if id is not None:
            self.id = id  # Assign provided ID if given
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  # Increment counter and assign new ID
