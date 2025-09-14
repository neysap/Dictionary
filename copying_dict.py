#Dictionaries - Copying
#Be careful when you try to copy a dictionary
#Like lists and other complex objects, assignment is done by reference
#This WILL NOT copy a dictionary
person = {'status': 'perfection', 'age': 22}
person_clone = person #creates a new reference to the same object
person_clone['status'] = 'less than perfect'
print(person['status']) #changes variable the person...it’s now ‘less than perfect’ for original person
print(person_clone is person) #True... point to the same object so IT WON'T COPY TO A DICTIONARY

#But this WILL copy a dictionary
person = {'status': 'perfection', 'age': 22}
person_clone2 = person.copy() #creates a new reference to a new object
person_clone2['status'] = 'less than perfect'
print(person['status']) #it’s still ‘perfect’ for original person
print(person_clone2 is person) #False
#Also similar to lists and other complex objects, dictionaries are passed to functions by reference


# What if our dictionary is compound, and contains other complex objects?
multifaceted_person = {'status': 'multifaceted', 'age': 22, 'skills': ['music', 'art', 'programming']}
#SINCE SKILLS IS A LIST ITS A NESTED COMPOUND OBJECT

# Perform a deep copy
import copy
another_multifaceted_person = copy.deepcopy(multifaceted_person)

# Change the original person
multifaceted_person['skills'].append('gardening')

# Print results
print(multifaceted_person)
# print original person {'status': 'multifaceted', 'age': 22, 'skills': ['music', 'art', 'programming', 'gardening']}

print(another_multifaceted_person)  # print new reference to different person
#PRINTS THE DEEP COPY: {'status': 'multifaceted', 'age': 22, 'skills': ['music', 'art', 'programming']}

