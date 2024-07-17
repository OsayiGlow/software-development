import random
import time

# # Start the timer
# start_time = time.time()

# # Initialize an empty list
# h = []

# # Append random integers to the list and print progress
# for a in range(10000):
#     h.append(random.randint(0, 999))
#     print(f"done number {a}")

# # End the timer
# end_time = time.time()

# # Calculate the elapsed time
# elapsed_time = end_time - start_time

# # Print the list (this will be very large)
# print(h)

# # Print the elapsed time
# print(f"Time taken to complete: {elapsed_time} seconds")


# my_tuple = (1, 2, 3, "hello", 4.5, "life", 55, 9.3, "tsl", True)

# print(my_tuple[5:])



def laptop(brand, size, color, battery_life =100):
    print(f"Hi, We got a new laptop for sale, it is {brand} laptop, its size is {size} inches,color is {color},batttery life is {battery_life}")


#laptop("HP",15, "Black")



class TLS_Staff:
    def __init__(self, name:str, age:int,gender:str, position, new_staff= False,  **kwargs):
        self.name = name
        self.age = age
        self.gender = gender
        self.new_staff = new_staff
        self.position = position
        self.email = kwargs.get('email', None)
        self.religion = kwargs.get('religion', None)
        self.hobby = kwargs.get('hobby', None)   
    
    def __str__(self):
        attrs = [
            f"Name: {self.name}",
            f"Age: {self.age}",
            f"Gender: {self.gender}",
            f"Position: {self.position}",
            f"New Staff: {self.new_staff}",
            f"Email: {self.email}",
            f"Religion: {self.religion}",
            f"Hobby: {self.hobby}"
            "\n\n"
        ]
        return "\n".join(attrs) 
    
    
    
    


my_name = input("Enter your Name")
my_age = int(input("Enter your age"))
my_gender = input("What is your Gender?")
my_position = input("What is your Gender?")


staff = TLS_Staff()

print(staff)


# Glory = TLS_Staff("Glory",15,"Female", "Staff", True, email= "glory@gmail.com", hobby="Cooking")
# print(Glory)

# Stephen.email ="Stephen@gmail.com"
# Stephen.age =30
# print(Stephen)