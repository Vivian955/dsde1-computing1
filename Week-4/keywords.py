'''
keywords.py
Create functions that use keyword arguments
with default values.
'''

def welcome_message( user_name, place ):
    if input= user_name:
        return "Hello and welcome"
    elif:
        return "Hello,<user_name>, and welcome"
    elif input (place) = '':
        return "Hello and welcome to <place>"
    else input (user_name, place) = '','':
        return "Hello, <user_name>, and welcome to <place>"


# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>

def list_average()
# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list