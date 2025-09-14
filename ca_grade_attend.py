#Here’s a grade / attendance book for a teacher's students
#       It contains a  dictionary of dictionaries

# create a dictionary for each student
billy = {
    'name': 'Billy',
'grades' : [100, 80, 67, 100, 89],
'attendance': [True, True, True, True, True]
}
sarah = { 'name': 'Sarah',
          'grades': [0, 99, 0, 100, 0],
        'attendance': [True, False, True, False, True]
}
ben = {
    'name': 'Ben',
    'grades': [60, 82, 71, 92, 100],
    'attendance': [False, False, False, False, False]
}

# add each student to a dictionary using a unique student ID
students = {'1': billy, '2': sarah, '3': ben}

#Get the length (number) of students
print(len(students)) #number of keys... 3
#Get all the student IDs (keys) by using the built-in dict keys method
print(students.keys()) #prints dict_keys object containing unordered keys...   dict_keys(['1', '2', '3'])
#Note, since dictionaries are unordered, there is no guaranteeing the order of keys
#           But, you can sort
print(sorted(students.keys()))  # prints sorted list of keys... ['1', '2', '3']

# You can also get the keys by iterating over a dictionary itself
for k in students:
    print('key:', k) #key: 1    key: 2  key: 3

#Get Billy’s attendance
billy = students['1']
print(billy['attendance']) #[True, True, True, True, True]
#Get Sarah’s grades
sarah = students.get('2')
print(sarah.get('grades')) #[0, 99, 0, 100, 0]
#Use the built-in dict items method to get all key:value pairs for a dictionary... in this case, associated with ben
ben = students.get('3')
items = ben.items() #returns the sequence of tuples(key:value), 1st item key, 2nd item value
for key, val in items:
    print(key, val) #name Ben   grades [60, 82, 71, 92, 100]    attendance [False, False, False, False, False]


#Let’s get the average student grade for all assignments
grades = [] #create empty list to put info into
items = students.items() #returns the sequence of tuples(key:value)
for key, val in items: #iterate over student dictionaries #in this case the key is the student id and val is student
    for g in val['grades']: #iterate over student lists of grades val[]...whatever is in brackets is what we're iterating
        grades.append(g) #add it to our empty list
#prints average grades
print(round(sum(grades) / len(grades))) #69

#Here’s an even easier way -- just concatenate the lists
grades_concatenated = []
items = students.items() #iterate over student dictionaries
for key, val in items:
    grades_concatenated += val['grades'] #concatenate student lists of grades
print(round(sum(grades_concatenated) / len(grades_concatenated))) #69
 