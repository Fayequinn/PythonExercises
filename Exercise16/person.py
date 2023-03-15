class Person:
    number_of_persons = 0
    def __init__(self, name, age,  gender, id_number):
        self._name = name
        self._age = age
        self._gender = gender
        self._id_number = id_number
        Person.number_of_persons += 1

    def personal_details(self):
        return (self._name + ", " + self._age +" years old, " + self._gender)

    def display_id(self):
        return ("Name: " + self._name + ", ID: " + self._id_number)
