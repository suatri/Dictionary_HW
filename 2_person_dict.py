person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

# print(person)

#  print out the name of the second child
# print(person["children"][1])

# print out the name of the cat
# print(person["pets"]["cat"])

# use a loop to print out he names of each child

for x in person["children"]:
    print(x)


# use a loop to print out the pets in the following format
# The type of pet is: dog and the name of the pet is : Fido

variable = person["pets"]

for key, value in variable.item():
    print(f"the type of pet is: {key} and the name of the pet is: {value}")
