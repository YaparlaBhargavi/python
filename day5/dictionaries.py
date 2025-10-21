customer={
    "name":"john smith",
    "age":30,
    "is_verified":True
}
print(customer["name"])
# print(customer["birthdate"])   it is error because there is no birthdate in key 
# print(customer["Name"]) it is also error because we have name not Name
print(customer.get("birthdate")) #it prints none 
customer["name"]="jack"
print(customer["name"])
print(customer.get("birthdate","jan 1 2025"))  
