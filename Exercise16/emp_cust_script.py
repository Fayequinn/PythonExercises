from person import Person
from employee import Employee
from customer import Customer

person1=Person("Faye", "34", "F", "1234")

print(person1.personal_details())
print(person1.display_id())

emp1 = Employee("Sarah", "39", "F", "3210", "Teacher", 35000)
print(emp1.get_post_details())
print(emp1.personal_details())
print(emp1.display_id())
new = emp1.give_raise(5000)
print(new)
print(emp1.get_post_details())

customer1 = Customer("Carl", "44", "M", "4567", "Gold", 1400)
print(customer1.get_cust_dets())
print(customer1.reward(130))
print(customer1.get_cust_dets())

# example of polymorphism
print(emp1.display_id())
print(customer1.display_id())

print(Person.number_of_persons)
print(Customer.number_of_customers)
print(Employee.number_of_employees)


