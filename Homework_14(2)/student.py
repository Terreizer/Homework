class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} age, Gender: {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name}, Age: {self.age}, Gender: {self.gender}, Record Book: {self.record_book}"

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))