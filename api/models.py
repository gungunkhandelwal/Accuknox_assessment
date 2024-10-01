from django.db import models

class Person(models.Model):
    name=models.CharField(max_length=100,default='name')
    age=models.IntegerField(null=True,blank=True,default=0)
    data=models.CharField(max_length=50,default='fill')

    def __str__(self):
        return self.name


class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self._attributes = [
            {'length': self.length},
            {'width': self.width}
        ]
        self._index = 0  # To keep track of iteration

    def __iter__(self):
        # Reset the index for a new iteration
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self._attributes):
            result = self._attributes[self._index]
            self._index += 1
            return result
        else:
            # Stop iteration when all attributes are returned
            raise StopIteration

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
