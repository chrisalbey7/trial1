"""
this
is
an
example
of
a
multi
line
comment
"""

print("Hello World!")

# Get user input, init variables
character_name = input("What's your name ")
character_name = character_name.capitalize()
character_age = int(input("How old are you? "))
character_place = input("Where are you from? ")
character_place = character_place.capitalize()
character_flavour = input("Which is your favourate icecream flavour? ")

# checks the age and assigns a bool value to y (comparison operator) to assign it to a specefic age group
y = (character_age <= 19 and character_age >= 10)
if y == True:
    age_group = "boy"
elif character_age <= 10:
    age_group = 'kid'
else:
    age_group = "man"


# Function that describes the intro story
def story():
    print('')
    print("Story")
    print('')
    print('There once was a ', character_age, " year old ", age_group, "named", character_name, ",")
    print(character_name + " likes " + character_flavour + " icecream.")
    print(
        character_name + " grew strong by eating " + character_flavour + " icecream, until one day, a strange thing happened!!")
    print(character_name + "\'s village " + character_place + " ran out of all the " + character_flavour + " icecreams")


# Ready to play?
def main():
    print('')
    enter = str(input("Do you want to begin this adventure? (Y/N)"))
    if enter == "Y":
        return game_mode()
    elif enter == "y":
        return game_mode()
    else:
        print("OK tell me when you're ready")
        enter2 = input("Are you ready? ")
    if enter2 == "Y":
        return game_mode()
    elif enter2 == "y":
        return game_mode()
    else:
        input("Wrong input try again")


# program to set username
def username():
    userID = str(
        character_place.upper()[0] + character_place.upper()[1] + character_name.upper()[0] + character_name.upper()[
            1] + character_name.upper()[2]) + str(character_age)
    print("USER ID: " + userID)
    return userID


# Surprise!
def game():
    print('')
    username()
    print("Hello gamer, Fuck you! find some real game bruhh...! :) ")


# Excited to play?
def game_mode():
    z = input("Let's collect all the ice creams!! : (Y/N)")
    if z == "Y":
        return game()
    elif z == "y":
        return game()
    else:
        print('Wrong input... Try again!')


# Here goes my First application
story()
main()

# login user, new user page
# login page
# regestration page
