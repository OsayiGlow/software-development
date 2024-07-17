# data = input("enter number")
# data = int(data)

# if data %7 ==0:
#     print("Holla! Number is Multiple of 3")
# else:   
#     if data %2 ==0:
#       print("Holla! Number is Multiple of 2")
      
#     else:
#          print("Odd...... Number!")


# # Program to check if a number is prime or not

num = 2978483

# To take input from the user

num = int(input("Enter a number: "))

# define a flag variable
flag = True

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        remainder = num % i
        #print(f"printing {num}%/ {i}:", remainder)
        if remainder == 0:
            print(f"Number {num} is not a prime number")
            flag = False
            break
       
           
    
    if flag == True:
      print(f"Number  is a prime number")

            
        
         