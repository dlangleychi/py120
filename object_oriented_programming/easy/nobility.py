class WalkingMixin:
    def walk(self):
        return f'{self.name} {self.gait()} forward'
    
class Noble(WalkingMixin):
    def __init__(self, name, title):
        self._name = name
        self._title = title

    @property
    def name(self):
        return self._name
    
    @property
    def title(self):
        return self._title
    
    def gait(self):
        return 'struts'
    
    def walk(self):
        return f'{self.title} {super().walk()}'
    
byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"