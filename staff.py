


class TSL_Staff:
    def __init__(self, name:str, age:int,gender:str, position, new_staff= False,  **kwargs):
        self.name = name
        self.age = age
        self.gender = gender
        self.new_staff = new_staff
        self.position = position
        self.email = kwargs.get('email', None)
        self.religion = kwargs.get('religion', None)
        self.hobby = kwargs.get('hobby', None)  
        self.portfolio ={}
    
    def __str__(self):
        attrs = [
            f"Name: {self.name}",
            f"Age: {self.age}",
            f"Gender: {self.gender}",
            f"Position: {self.position}",
            f"New Staff: {self.new_staff}",
            f"Email: {self.email}",
            f"Religion: {self.religion}",
            f"Hobby: {self.hobby}",
             f"Portfolio: {self.portfolio}"
            
            "\n\n"
        ]
        return "\n".join(attrs) 
    

    def removeHobby(self):
        self.hobby = None or ''

    def removePosition(self):
        self.position = None or ''

    def addPortfolio(self,portofolio:dict):
        for key,value in portofolio.items():
          #  print(key,value )
            self.portfolio[key] = value





