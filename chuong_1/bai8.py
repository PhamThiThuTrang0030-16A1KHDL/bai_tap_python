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


class Employee:
    def __init__(self, name, dob, join_date):
        self.name = name
        self.dob = dob
        self.join_date = join_date

    def display(self):
        return f"Name: {self.name}, Date of Birth: {self.dob.display()}, Join Date: {self.join_date.display()}"


dob = Date(1, 1, 1990)
join_date = Date(1, 1, 2020)
employee = Employee("Nguyen Van A", dob, join_date)
print(employee.display())
