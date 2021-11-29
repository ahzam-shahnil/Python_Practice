class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        if not self.validate():
            raise ValueError("Invalid Date")

    def validate(self):
        if 1 <= self.day <= 30 and 1 <= self.month <= 12:
            return True
        else:
            return False

    def later_than(self, other):
        first = (self.day, self.month, self.year)
        second = (self.day, self.month, self.year)
        return first > second
    # def increment_month(self, month):
    #     sel.
