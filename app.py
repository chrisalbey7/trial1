print("Hello World!")
character_name = input("What's your name ")
character_age = int(input("How old are you? "))
character_place = input("Where are you from? ")
character_flavour = input("Which is your favourate icecream flavour? ")

y = ( character_age <= 19 and character_age >= 10)
# checks the age and assigns a bool value to y (comparison operator)
if y == True:
    age_group = "boy"
#if y is true age_group is assigned the value
elif character_age <= 10:
    age_group = 'kid'
else:
    age_group = "man"
print("Story")
''
print('There once was a ', character_age , " year old ", age_group, "named", character_name, ",")
print(character_name + " likes " + character_flavour + " icecream.")
print(character_name + " grew strong by eating " + character_flavour + " icecream, until one day, a strange thing happened!!")
print(character_name, "s village " + character_place+ " ran out of all the "+ character_flavour + "icecreams")

"""
this is an example of a 
multi 
line 
comment
"""

