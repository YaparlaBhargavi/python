def greet_user(first_name,last_name):
    print(f'hi {first_name}{last_name}')
    print("welcome aboard")
    
    
print("start")

'''greet_user("john") #it gives error becoz we didnt provide last_name 
greet_user("jon","smith") -------->  postional arguments
greet_user(last_name="smith",first_name="john")#keyword arguments
calc_cost=(total=50,shipping=5,discount=0.1) #here we can use keyword arg becoz by seeing numbers we cant tell what are they so keyword arg helps to out easily to find'''

print("finish")