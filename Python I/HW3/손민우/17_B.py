# 1
'''
Hello, Jesse!
'''
#2
'''
I have a dog.
My dog's name is Willie.
My dog's name is Willie.

I have a hamster.
My hamster's name is Harry.
My hamster's name is Harry.
My hamster's name is Harry.
'''

# 3
'''
Jimi Hendrix
John Lee Hooker
'''

# 4
'''
{'first': 'jimi', 'last': 'hendrix', 'age': 27}
'''

# 5
'''
Hello, Hannah!
Hello, Ty!
Hello, Margot!
'''

# 6
'''
Printing model: iphone case
Printing model: robot pendant
Printing model: dodecahedron

The following models have been printed:
iphone case
robot pendant
dodecahedron
'''

# 7
'''
Making a 16-inch pizza with the following toppings:
- peperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
'''

# 8
'''
{'first_name': 'albert', 'last_name': 'einstein', 'location': 'princeton, 'field': 'physics'}
'''

# 9
'''
Making a 16-inch pizza with the following toppings:
- peperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
'''

# 10
'''
My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.

My dog's name is Lucy.
My dog is 3 years old.
Lucy is now sitting.
'''

# 11
'''
2013 Subaru Outback
This car has 23500 miles on it.
This car has 23600 miles on it.
'''

# 12
'''
2016 Tesla Models s
This car has a 60-kWh battery.
'''

# 13
'''
2015 Audi A4
This car has 23 miles on it.
'''

# 14
'''
2015 Volkswagen Beetle
2015 Tesla Roadster
'''

# 15
'''
Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.
'''
from collections import OrderedDict # 순서를 기억하는 dict

favorite_language = OrderedDict()

favorite_language['jen'] = 'python'
favorite_language['sarah'] = 'c'
favorite_language['edward'] = 'ruby'
favorite_language['phil'] = 'python'

for name, language in favorite_language.items():
	print(name.title() + "'s favorite language is "+ language.title()+".")