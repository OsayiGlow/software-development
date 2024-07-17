
from staff import TSL_Staff 


class Staff(TSL_Staff):
    def __init__(self, name: str, age: int, gender: str, position, new_staff=False, child =True, **kwargs):

        super().__init__(name, age, gender, position, new_staff, **kwargs)



mystaff = Staff("name", 29,"43","CEO")

print(mystaff)

