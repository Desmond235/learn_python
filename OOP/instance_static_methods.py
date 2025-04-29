class Employee:
    def __init__(self,name, position):
        self.name = name
        self.position =  position

    def get_info(self):
        return f'{self.name} = {self.position}'

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]

        if position in valid_position:
            print(f'{position} is a valid position')
        else:
            print(f'{position} is not a valid position')
        return position


employee1 = Employee("Desmond", "Manager")
employee2 = Employee("Francis", 'Cook')

print(employee1.name)
print(employee1.position)
print(employee1.get_info())
print(Employee.is_valid_position(employee1.position))