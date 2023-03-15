from person import Person

class Customer(Person):

    number_of_customers = 0

    def __init__(self, name, age, gender, id_number, member_type, points):
        self._member_type = member_type
        self._points = points
        super().__init__(name, age, gender, id_number)
        Customer.number_of_customers += 1

    def get_cust_dets(self):
        return (self._name + ": " + self._member_type + " Customer, " + str(self._points) + " points." )

    def reward(self, spend):
        if 10 < spend <= 50:
            self._points = self._points + 10
        elif 50 < spend <= 100:
            self._points = self._points + 20
        elif spend > 100:
            self._points = self._points + 30
        return self._points

# polymorphism
    def display_id(self):
        return ("Name: " + self._name + ", Account number: " + self._id_number)

