# 3-1
# bicycles = ['trek', 'cannondale','redline','specialized']
# message="My first bicycle was a " + bicycles[0].title()+"."
# print(message)
# ----------------------------------
# My first bicycle was a Trek.

# 3-2
# motorcycles = ['honda','yamaha','suzuki','ducati']
# print(motorcycles)
#
# too_expensive='ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("\nA " + too_expensive.title() + " is too expensive for me.")
# --------------------------------
# ['honda', 'yamaha', 'suzuki', 'ducati']
# ['honda', 'yamaha', 'suzuki']
#
# A Ducati is too expensive for me.
#

# 3-3
# cars=['bmw','audi','toyota','subaru']
# print("Here is the original list:")
# print(cars)
#
# print("\nHere is the sorted list:")
# print(sorted(cars))
#
# print("\nHere is the reverse alphabetical list:")
# print(sorted(cars,reverse=True))
#
# print("\nHere is the original list again:")
# print(cars)
# -------------------------------------------
# Here is the original list:
# ['bmw', 'audi', 'toyota', 'subaru']
#
# Here is the sorted list:
# ['audi', 'bmw', 'subaru', 'toyota']
#
# Here is the reverse alphabetical list:
# ['toyota', 'subaru', 'bmw', 'audi']
#
# Here is the original list again:
# ['bmw', 'audi', 'toyota', 'subaru']

# 4-1
# magicians=['alice','david','carolina']
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
#     print("I can't wait to see your next trick, "+ magician.title() + ".\n")
#
# print("Thank you everyone that was a great magic show!")
# ------------------------------------------------------
# Alice, that was a great trick!
# I can't wait to see your next trick, Alice.
#
# David, that was a great trick!
# I can't wait to see your next trick, David.
#
# Carolina, that was a great trick!
# I can't wait to see your next trick, Carolina.
#
# Thank you everyone that was a great magic show!

# 4-2
# numbers = list(range(1,6))
# print(numbers)
# ---------------------
# [1, 2, 3, 4, 5]


# 4-3
# even_numbers=list(range(2,11,2))
# print(even_numbers)
# ----------------------------
# [2, 4, 6, 8, 10]

# 4-4
# squares = []
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
# print(squares)
# ---------------------------
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 4-5
# players = ['charles','martina','michael','florence','eli']
#
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())
# -------------------------------------
# Here are the first three players on my team:
# Charles
# Martina
# Michael

# 4-6
# my_foods=['pizza','falafel','carrot cake']
# friend_foods = my_foods[:]
#
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print("My favorite foods are:")
# print(my_foods)
#
# print("\nMy friend's favorite foods are:")
# print(friend_foods)
# ----------------------------------------------
# My favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'cannoli']
#
# My friend's favorite foods are:
# ['pizza', 'falafel', 'carrot cake', 'ice cream']

# 4-7
# dimensions = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
#
# dimensions = (400,100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)
# -----------------------------------
# Original dimensions:
# 200
# 50
#
# Modified dimensions:
# 400
# 100

# 5-1
# cars = ['audi','bmw','subaru','toyota']
# for car in cars:
#     if car=='bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# -------------------------
# Audi
# BMW
# Subaru
# Toyota


# 5-2
# available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni','pineapple','extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print("Adding " + requested_topping + ".")
#     else:
#         print("Sorry, We don't have " + requested_topping + ".")
# print("\nFinished making your pizza!")
# ------------------------------------------------
# Adding mushrooms.
# Sorry, We don't have french fries.
# Adding extra cheese.
#
# Finished making your pizza!

# 5-3
# answer = 17
# if answer != 42:
#     print("That is not the correct answer. Please try again!")
# ---------------------------------------------------------
# That is not the correct answer. Please try again!

# 5-4
# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'
#
# if user not in banned_users:
#     print(user.title()+ ", you can post a response if you wish.")
# ----------------------------------------------------
# Marie, you can post a response if you wish.

# 5-5
# age=17
# if age >= 18:
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")
# --------------------------------------------
# Sorry, you are too young to vote.
# Please register to vote as soon as you turn 18!

# 5-6
# age=12
# if age<4:
#     price=0
# elif age<18:
#     price=5
# elif age<65:
#     price=10
# elif age >= 65:
#     price=5
# print("Your admission cost is $" +str(price) + ".")
# --------------------------------------------------
# Your admission cost is $5.

# 5-6
# age=12
# if age<4:
#     price=0
# elif age<18:
#     price=5
# elif age<65:
#     price=10
# else:
#     price=5
# print("Your admission cost is $" +str(price) + ".")
# ------------------------------------------
# Your admission cost is $5.

# 6-1
# alien_0 = { 'x_position':0, 'y_position':25, 'speed':'medium' }
# print("Original position:" +str(alien_0['x_position']))
#
# if alien_0['speed'] == 'slow':
#     x_increment =1
# elif alien_0['speed'] == 'medium':
#     x_increment =2
# else:
#     x_increment =3
# alien_0['x_position']=alien_0['x_position']+x_increment
# print("New position: " +str(alien_0['x_position']))
# ---------------------------------------------------
# Original position:0
# New position: 2


# 6-2
# favorite_languages={'jen':'python', 'sarah':'c', 'edward':'ruby','phil':'python'}
#
# for name, language in favorite_languages.items():
#     print(name.title()+"'s favorite language is " + language.title())
# --------------------------------------------------------------
# Jen's favorite language is Python
# Sarah's favorite language is C
# Edward's favorite language is Ruby
# Phil's favorite language is Python


# 6-3
# user_0 = {'username':'efermi','first':'enrico', 'last':'fermi'}
#
# for key,value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)
# ------------------------------
#
# Key: username
# Value: efermi
#
# Key: first
# Value: enrico
#
# Key: last
# Value: fermi

# 6-4
# aliens = []
#
# for alien_number in range(0,30):
#     new_alien = {'color':'green' , 'points': 5, 'speed' :'slow'}
#     aliens.append(new_alien)
#
# for alien in aliens[0:3]:
#     if alien['color']=='green':
#         alien['color']='yellow'
#         alien['speed']='medium'
#         alien['points']=10
#     elif alien['color']=='yellow':
#         alien['color']='red'
#         alien['speed']='fast'
#         alien['points']=15
#
# for alien in aliens[0:5]:
#     print(alien)
# print("...")
#
#---------------------------------------------------------
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'yellow', 'points': 10, 'speed': 'medium'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# ...


# 6-5
# pizza = {'crust':'thick','toppings':['mushrooms', 'extra cheese']}
# print("You ordered a " + pizza['crust']+ "-crust pizza " + "with the following toppings:")
#
# for topping in pizza['toppings']:
#     print("\t" + topping)
#-----------------------------------------------------------------
# You ordered a thick-crust pizza with the following toppings:
# 	mushrooms
# 	extra cheese


#6-6
# users = {'aeinstein': {'first':'albert', 'last':'einstein', 'location':'princeton'},
#          'mcurie':{'first':'marie', 'last': 'curie', 'location':'paris'}}
#
# for username, user_info in users.items():
#     print("\nUsername: " + username)
#     full_name = user_info['first']+ " " + user_info['last']
#     location = user_info['location']
#
#     print("\tFull name: " + full_name.title())
#     print("\tLocation: " + location.title())
#-----------------------------------------------------
# Username: aeinstein
# 	Full name: Albert Einstein
# 	Location: Princeton
#
# Username: mcurie
# 	Full name: Marie Curie
# 	Location: Paris

#7-1
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
#
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

#7-2
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "
#
# name= input(prompt)
# print("\nHello, " +name + "!")

#7-3
# height = input("How tall are you, in inches? ")
# height = int(height)
#
# if height >= 36:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'ii be able to ride when you're a little older.")

#7-4
# number = input("Enter a number, and I'll tell you if it's even or odd: ")
# number=int(number)
#
# if number % 2==0:
#     print("\nThe number " +str(number) + " is even.")
# else:
#     print("\nThe number " +str(number) + " is odd.")


#7-5
current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
# ------------------------------
# 1
# 2
# 3
# 4
# 5


#7-6
# prompt = "\nPlease tell me a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"
#
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("I'd lover to go to " +city.title() + "!")

#7-7
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users=[]
#
# while unconfirmed_users:
#     current_user= unconfirmed_users.pop()
#     print("Verifying user: " + current_user.title())
#     confirmed_users.append(current_user)
#
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())
# -------------------------------------------------
# Verifying user: Candace
# Verifying user: Brian
# Verifying user: Alice
#
# The following users have been confirmed:
# Candace
# Brian
# Alice

#7-8
# pets=['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
#
# while 'cat' in pets:
#     pets.remove('cat')
#
# print(pets)
# -------------------------
# ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# ['dog', 'dog', 'goldfish', 'rabbit']


#7-9
# responses={}
# polling_active = True
#
# while polling_active:
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#
#     responses[name]=response
#
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no' :
#         polling_active = False
#
# print("\n--- Poll Results ---")
# for name,response in responses.items():
#     print(name + " would like to climb " + response + ".")

