class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self): 
        return self._items

    @property
    def to_do(self): 
        output = []

        for item in self._items:
            if item.status == "Not Started":
                output.append(item)

        return output

    @property
    def doing(self): 
        return self._items

    @property
    def done(self): 
        return self._items

