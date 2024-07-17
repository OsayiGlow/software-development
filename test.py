
from staff import TSL_Staff as staff


mystaff = staff("name",20,"M","Manager",new_staff=True, religion = "Christian")
mystaff.hobby = "Reading"

print(mystaff)

mystaff.addPortfolio({"Work_Experience":"7 Years", "Relationship_Status":"Single"})

print(mystaff)