#this initializes an empty dictionary
courses = {}
#Then add elements
courses["CIT590"] = "Intro to Programming" #we set key CIT590 to value = intro to...
courses.update({"CIS545": 'Big Data'}) #anotehr way to add to dictionary
print(courses.get('CIS545')) #view input

#Or create a dictionary from a list of tuples using the dict function ... each tuple has two items
translation = dict([(1, 'uno'), (2, 'dos'), (3, 'tres')]) #1st item is the key, 2nd item is the associated value
print(translation[1])#prints uno

#You can also create a dictionary from 2 separate lists
#Here’s a list of keys
keys_lst = ['Joey', 'Fred', 'Katie']
#And a list of values
values_lst = [6, 4, '2 months']
#Make a sequence of tuples using the built-in zip function
zipped = zip(keys_lst, values_lst)
print(type(zipped)) #The type is zip... <class 'zip'>
#Then create a dictionary from the zip using the dict function
kids_ages = dict(zipped)
print(kids_ages) #{'Joey': 6, 'Fred': 4, 'Katie': '2 months'}
print(kids_ages['Fred']) #value associated with key 'fred'... we get 4
