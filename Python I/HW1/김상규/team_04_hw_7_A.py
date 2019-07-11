# 3-1 bicycles.py
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycles was a " + bicycles[0].title() + "."
print(message)

# 3-2 motorcycles.py
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

# 3-3 cars.py
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list: ")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the reverse alphabetical list:")
print(sorted(cars, reverse=True))
print("Here is the original list again: ")
print(cars)

# 4-1 magicians.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone, that was a great magic show!")

# 4-2 numbers.py
numbers = list(range(1, 6))
print(numbers)

# 4-3 even_numbers.py
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 4-4 squares.py
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

# 4-5 players.py
players = ['chares', 'mattina', 'michael', 'florence', 'eli']
print("Here are the first thress players on my team:")
for player in players[:3]:
    print(player.title())
    
# 4-6 foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)     

print("\nMy friend's favorite foods are:")
print(friend_foods)
    
 
# 4-7 dimensions.py
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    

# 5-1 cars.py
cars = ['audi', 'bmw', 'subaru', 'toyota']
    
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else: 
        print(car.title())
        
# 5-2 toppings.py
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else: 
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")


# 5-3 magic_number.py
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")


# 5-4 banned_users.py
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish")

# 5-5 voting.py
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

        
        
    
# 5-6 amusement_park.py
age = 12
if age<4:
    price = 0
elif age<18:
    price = 5
elif age<65:
    prie = 10
elif age>=65:
    prie = 5
    
print("Your admission cost is $" + str(price) + ".")

if age<4:
    price = 0
elif age<18:
    price = 5
elif age<65:
    prie = 10
else:
    prie = 5
    
print("Your admission cost is $" + str(price) + ".")



# 6-1 alien.py
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: 
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New position: " + str(alien_0['x_position']))



# 6-2 favorite_languages.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
    
    
# 6-3 user.py
user_0 = {'username': 'efermi', 
         'first': 'enrico',
         'last': 'fermi',
         }
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)
    

# 6-4 aliens.py
aliens = []
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
for alien in aliens[0:5]:
    print(alien)
print("...")


# 6-5 pizza.py
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print("You ordered a " + pizza['crust'] + "-crust pizza " + 
     "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)


# 6-6 many_users.py
users = {'aeinstein': {'first': 'albert',
                      'last': 'einstein',
                      'location': 'princeton'},
        'mcurie': {'first': 'marie',
                  'last': 'curie',
                   'location': 'paris',}
        }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    
    
# 7-1 parrot.py
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit to end the program."

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else: 
        print(message)
        
        
# 7-2 greeter.py
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print("\nHello, " + name + "!")


# 7-3 rollercoaster.py
height = input("How tall are you, in inches?")
height = int(height)
if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
    

# 7-4 even_or_odd.py
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number %2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")


# 7-5 counting.py
current_number = 1
while current_number <=5:
    print(current_number)
    current_number += 1
    

# 7-6 cities.py
prompt = "\nPlease tell me a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd loe to go to "  + city.title() + "!")
        

# 7-7 confirmed_users.py
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    
    
# 7-8 pets.py
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)


# 7-9 mountain_poll.py
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
