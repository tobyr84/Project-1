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
        output = []

        for item in self._items:
            if item.status == "In Progress":
                output.append(item)

        return output

    @property
    def done(self): 
        output = []

        for item in self._items:
            if item.status == "Completed":
                output.append(item)

        return output

    @property
    def show_all_done_items(self):
        # if there are 5 or fewer completed tasks

        output = []

        for item in self._items:
            if item.status == "Completed":
                output.append(item)

        if len(output) <= 5:
            return True
        else:
            return False

        # output - a list
        # 5      - a number
        # len()  - a function that takes lists, and returns numbers
        # <=     - an operator that takes two numbers, and returns true or false
        # if     - a construct that takes true or false