class Transform:

    @classmethod
    def lowercase(cls, string):
        return string.lower()

    def __init__(self, string):
        self._string = string
    
    @property
    def string(self):
        return self._string
    
    def uppercase(self):
        return self.string.upper()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz