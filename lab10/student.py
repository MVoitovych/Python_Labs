class Student:
    def __init__(self, name, surname, rating, group, birth_year) -> None:
        self.name = name
        self.surname = surname
        self.rating = rating
        self.group = group
        self.birth_year = birth_year

    # def __eq__(self, other):
    #     return self.rating == other.rating

    def __lt__(self, other):
        return self.rating < other.rating

    def __le__(self, other):
        return self.rating <= other.rating

    def __gt__(self, other):
        return self.rating > other.rating

    def __ge__(self, other):
        return self.rating >= other.rating

    def __str__(self):
        return f"Student {self.name} {self.surname} with {self.rating} rating, from {self.group} "