from person import Person

class Employee(Person):
    number_of_employees = 0
    def __init__(self, name, age, gender, id_number, post, salary):
        self._post = post
        self._salary = salary
        super().__init__(name, age, gender, id_number)
        Employee.number_of_employees += 1

    def get_post_details(self):
        return (self._post + ", " + str(self._salary))

    def give_raise(self, rise):
        self._salary = self._salary + rise
        return self._salary
