
# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 

# Use input to collect each word to a variable
# Use an f string to display the story

# Your madlib must collect at least 6 words!

# Madlib variables
name = input("Who are you? ")
buddy = input("Who is your adventure buddy? ")
fear = input("What creature do you fear? ")
food = input("What is your favorite cuisine? ")
country = input("Name a country you want to travel to! ")
song = input("What is your favorite song? ")

# Madlib Story Time!
print(f"Welcome to the THUNDER DOME {name}!!!")
print(f"You better have your adventure buddy, {buddy}, with you because this is gonna suck!")
print(f"You will soon be forced onto a plane heading to {country}, but not to eat your favorite {food}.....")
print(f"{country} is under attack a swarm of {fear}!!!")
print(f"Get mentally hyped for this battle because {song} will be on a forever loop until you defeat {fear}")
print("GOOD LUCK! :-0")

# --------------------------------------------------
# Partial solution


# name = input("Name:")
# color = input("color:")
# num = input("Number:")

# print(f"{name} wore {color} shoes while they counted to {num}")