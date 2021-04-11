students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]






#1 how many students are there
print('There are {} students'.format(len(students)))

#2 how many students prefer different coffee types?
count = 0
for student in students:
    if student['coffee_preference'] == 'light':
        count = count + 1
print('{} people prefer light coffee '.format(count))
count = 0
for student in students:
    if student['coffee_preference'] == 'medium':
        count = count + 1
print('{} people prefer medium coffee '.format(count))
count = 0
for student in students:
    if student['coffee_preference'] == 'dark':
        count = count + 1
print('{} people prefer dark coffee '.format(count))

#3
#How many types of each pet are there
#get list of all pets
list_of_all_species = []
for student in students:
    for species in student['pets']:
            list_of_all_species.append(species['species']) 

#list of unique pets to compare
list_of_unique_species =[]
for student in students:
    for species in student['pets']:
            if species['species'] not in list_of_unique_species:
                list_of_unique_species.append(species['species']) 
                
#compare both lists
count = 0
for i in list_of_unique_species:
    for j in list_of_all_species:
        if i == j:
            count += 1
    if(count == 1):
        print("There is {} {}".format(count, i))
    else:
        print("There are {} {}s".format(count, i))
    count = 0


#4 how many grades does each student have
same_grade_count = False
grade_count = 0
for student in students:
    grade_count = len(student['grades'])
    if grade_count == len(student['grades']):
        same_grade_count = True
    else:
        same_grade_count = False
        break
if same_grade_count == True:
    print('Each student has {} grades'.format(grade_count))
    print("Every student has the same amount of grades")
else:
    print("Every student doesnt have the same number of grades")



#5 what is each students avg
for student in students:
    total = sum(student['grades'])
    grades = len(student['grades'])
    avg = total/grades
    print('{} has an avg of {}'.format(student['student'], avg))


#6 how many pets does each student have
for student in students:
    if (len(student['pets']) )== 0:
        print('{} has no pets'.format(student['student']))
    elif (len(student['pets'])) == 1:
        print('{} has {} pet'.format(student['student'],len(student['pets'])))
    else:
        print('{} has {} pets'.format(student['student'],len(student['pets'])))


#7 how many students are in web development, data science
web_count = 0
ds_count = 0
for student in students:
    if student['course'] == 'web development':
        web_count += 1
    elif student['course'] == 'data science':
        ds_count += 1
print('{} students are in web development'.format(web_count))
print('{} students are in data science'.format(ds_count))



#8 what is the avg number of pets for students in web development 
pet_count = 0
student_count = 0
for student in students:
    if student['course'] == 'web development':
        pet_count = pet_count + len(student['pets'])
        student_count += 1
avg = int(pet_count / student_count)
print('The avg number of pets for students in web development is {}'.format(avg))


#9 what is the avg pet age for students in data science
sum_of_age = 0
num_of_pets = 0 
for student in students: 
    if student['course'] == 'data science':
        for pets in student['pets']:
            sum_of_age += pets['age']
        num_of_pets += len(student['pets'])
avg = int(sum_of_age / num_of_pets)
print('The avg pet age for students in data science is {}'.format(avg))


#10 what is the most frequent coffee preference for data science students
list_of_unique_coffee_types = []
list_of_all_coffees = []

#list of unique coffee types for data science students
for student in students: 
    if student['course'] == 'data science':
        if student['coffee_preference'] not in list_of_unique_coffee_types:
            list_of_unique_coffee_types.append(student['coffee_preference'])

# get all coffees for data science students
for student in students: 
    if student['course'] == 'data science':
            list_of_all_coffees.append(student['coffee_preference'])

#compare both lists 
count = 0
for i in list_of_unique_coffee_types:
    for j in list_of_all_coffees:
        if i == j:
            count += 1
    if(count == 1):
        print("{} data science student prefers {} coffee".format(count, i))
    else:
        print("{} data science students prefer {} coffee".format(count,i))
    count = 0












