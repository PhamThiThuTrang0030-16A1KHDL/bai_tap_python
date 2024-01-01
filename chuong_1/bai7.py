from datetime import datetime, timedelta

class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        return f"{self.day}/{self.month}/{self.year}"

    def next(self):
        current_date = datetime(self.year, self.month, self.day)
        next_date = current_date + timedelta(days=1)
        self.day = next_date.day
        self.month = next_date.month
        self.year = next_date.year


date = Date(31, 12, 2023)
print(date.display()) 
date.next()
print(date.display()) 
