#!/usr/bin/env python3 
import threading
print("   ........................................           ................................................")
print("v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v---OUTPUT---v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v^v")
print("   .........................................           ................................................")

#We want to learn about how to manipulae lists
#Below we show multiple ways a list can be made up of,
random_objects = [3.14 , "3,900", "more months to add"]
months = ["January", "February" , "March" , "April" ,"May", "June", "July" , "August" , "September" , "October"," November" , "December"]
numbers = [0 , 1 , 2 , 3 , 4 , 5 ,6 ,7, 8, 9]
random_numbers = [23, 453, 34, 21, 333]
#With a simple assign operator = we can copy lists into a new variable
#is the original list is changes, the object to which it was copied to initially will now change 
copy_randoms = random_objects
copy_months = months
#INSERT AND REVERSE 
random_objects.insert(3,"using insert")
print("using insert() in random_objects: "+ str(random_objects))
random_objects.reverse()
#How to print the list 
print("using reverse() in random_objects: "+ str(random_objects))
print("This is the months list" +str(months))
print("This is the numbers list" +str(numbers))
print("This is the copy" + str(copy_randoms))
print("This is the new value of random_objects BEFORE appending new value to listt:\n " + str(random_objects))
random_objects.append(555)
print("AFTER: \n " + str(random_objects))
#SLICING LISTS
#An important factor for lists in pyhon is understanding slicing

print("**********************************SLICING LISTS*********************************************")
print(str(months[-1])) #when using negative numbers, it is like using reverse order, therefore -1 is the last index, -2 is the second to last index and so on
print(str(months[3:6])) # it will print the element in index 3,4 and 5. 6 is the stopping point therefore it is not printed 
print(str(months[:3]) + str(months[3:])) # will print elements from index 0 - index 2, second str will print from element 3 to last 

#LEN: Method of lists, methods are object functions which typically have either a return value or edit on the list 
print("**********************************LEN*********************************************")
lenght_list = len(months)
print("Lenght of month list " + str(lenght_list))
print("*********************************MAX, MIN AND SORTED********************************************")
#MAX, MIN AND SORTED 
print(str(max(random_numbers)))
print(str(min(random_numbers)))
print(str(sorted(random_numbers)))

#JOIN : is a string method that takes a list of strings as an argument, and returns a string consisting of the list elements joined by a separator string
print("**********************************JOIN*********************************************")
join_list = "\n".join(months)
print("USING JOIN:\n" + str(join_list))
#Udacity example 
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

#Using mutability which is able in lists but not in strings, we will use a copy variable of a list 
copy_months[0] = "WINTER MONTH"
print("Copy list of months has been cahnged in index 0: ")
print(str(copy_months))
# Edit a list using slicing 
copy_months[5:7] = ["SUMMER", "SUMMER"]
print("NEW LIST USING SLICING AND MUTATION" + str(copy_months))

#TUPLES : ARE IMMUTABLE. Ex of when or why use tuples: used for things that are very close related like longitude and latitude
print("**********************************TUPLES*********************************************")
dimensions = 52, 40, 100
lenght, width, height = dimensions # this is called tuple unpacking 
#USING FORMAT ***************
print("The dimensions are  {} {} {}".format(lenght, width , height))
#Udacity example 
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

#SETS : A set is a data type for mutable unordered collections of unique elements. One application of a set is it remove duplicates from a list.
#sets are unordered so there is no "last element"
#has a pop() method - when use pop in a set, random elemnt is removed 
print("**********************************SETS*********************************************")
set_list_example = ["Mexico","Mexico","USA", "India"]
print("This is the list using a set:\n" + str(set(set_list_example)))
print("This is the list NOT USING a set:\n" + str(set_list_example))
set_list_example.pop()
print("This is the list using a set AND using its method pop():\n" + str(set(set_list_example)))
b_set_list = set(set_list_example)
b_set_list.add("Turkey")
print("This is the b_set_list using a set AND after using its method pop() AND using add():\n" + str(b_set_list))

#DICTIONARIES: A dictionary is a mutable data type that stores mappings of unique keys to values. 
#identity operators useful in data structures: in or not in, return boolean values 
print("**********************************DICTIONARIES*********************************************")
empty_dict = {}
empty_dict2 = dict()
languages = {"python":1, "Java" : 2, "C":3}
languages["LISP"] = 4
print("Check if C++ is in languages directory: ")
print( "C++" in languages) 
print("Check if Java is in languages directory: ")
print("Java" in languages)
print("C language key and value: ")
print(languages["C"])
#useful dictionary method: get()
get_a_language = languages.get("python")
print("Value retured using get for language python: " + str(get_a_language))
not_in_dict = languages.get("Not")
print("Value retured using get for language not in dictionary : " + str(not_in_dict))
#using lists as the value of a key
animals = {"cat": [11,22,33,44], "bird": [5,6,7]}
list_dic_value = animals["cat"][2]
print("This is the value in key 'cat' index 2: " + str(list_dic_value))


#NESTED DICTIONARY
print("********************************** NESTED DICTIONARIES *********************************************")
elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

states = { "Texas": {"country": "USA",
                    "population": 28.7,
                    },
          "Coahuila": {"country": "Mexico",
                       "population": 2.995} }
Coahuila_population = states["Coahuila"]["population"]
print("Variable with the value extracted from the nested Dictionary:  " + str(Coahuila_population))
mexico_dic = states["Coahuila"]
print("Variable with the dictionary extracted from the nested Dictionary:  " + str(mexico_dic))

#You can also add a new key to the element dictionary.
oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)

#Udacity Example:
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}
print("Element values of hydrogen BEFORE adding new value: " + str(elements['hydrogen']))
# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
elements['hydrogen']['is_noble_gas'] =  False 
elements['helium']['is_noble_gas'] = True
print("Element values of hydrogen AFTER adding new value: " + str(elements['hydrogen']))

#Udacity Example
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = verse.split()
print(set(verse_set), '\n')

# print the number of unique words
num_unique = len(set(verse_set))
print(num_unique, '\n')

#Udacity Example 
verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys()) # .keys() returns a list of all the keys
                                        #values() return a list of all the values 
                                        #.items() a list of (key, value) tuples

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1]) 

# Data Structure	Ordered	    Mutable	        Constructor	            Example
# List      		   YES          Yes	       [ ] or list()	     [5.7, 4, 'yes', 5.7]
# Tuple	               Yes          No	       ( ) or tuple()	     (5.7, 4, 'yes', 5.7)
# Set	               No	        Yes	       {}* or set()	         {5.7, 4, 'yes'}
# Dictionary	       No	        No**	    { } or dict()	     {'Jun': 75, 'Jul': 89}



#Functions 
print("********************************** FUNCTIONS *********************************************")
def subtract(a=0, b=0):
    return a - b
subtract(10,5) #would return 5
print("Value returned from using a def function in python: " + str(subtract(10,5)))

#CONTROL FLOW  
print("********************************** CONTROL FLOW *********************************************")