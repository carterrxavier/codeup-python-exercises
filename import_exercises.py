import function_exercises
import itertools
import json

#1 b
x = function_exercises.calculate_tip(.15,100)
print(x)

#1c in jupyter notebook


#2
x = len(list(itertools.product('abc', '123')))
print('{} number of combinations'.format(x))


y = len(list(itertools.combinations('abcd',2)))
print('{} number of combinations'.format(y))

z = len(list(itertools.permutations('abcd',2)))
print('{} number of combinations'.format(z))


#3
dataset =  json.load(open("/Users/xaviercarter/codeup_data_science/python-exercises/profiles.json"))

#total number of users
w = len(dataset)
print(f'{w} users total')

#total number of active users
count = 0
for user in dataset:
    if user['isActive'] == True:
        count += 1
print(f'{count} active users' )

#total number of inactive users
count = 0
for user in dataset:
    if user['isActive'] == False:
        count += 1
print(f'{count} inactive users' )

#grand total of balances for all users
grand_total = 0
for user in dataset:
    balance = user['balance']
    adj_balance = balance.replace("$",'').replace(',','')
    grand_total += float(adj_balance)
print('${:,.2f} is the grand balance for all users'.format(grand_total))

#avg balence per user
print('${:,.2f} is the avg balence for the dataset'.format(grand_total/w ))


#user with the lowest balance and highest balance
for user in dataset:
    balance = user['balance']
    adj_balance = balance.replace("$",'').replace(',','')
    user['balance'] =  float(adj_balance)
lowest = sorted(dataset, key=lambda k:k['balance'])
print('{} has the balance with {}'.format(lowest[0]['name'], lowest[0]['balance'])) 

highest = sorted(dataset, key=lambda k:k['balance'], reverse=True)
print('{} has the highest balence with {}'.format(highest[0]['name'], highest[0]['balance']))


#most and least common fruit

fruit_count = 0
unique_fruits = []
all_fruits = []
fruit_dict = []
for user in dataset:
    all_fruits.append(user['favoriteFruit'])

for user in dataset:
    if user['favoriteFruit'] not in unique_fruits:
        unique_fruits.append(user['favoriteFruit'])

for i in unique_fruits:
    for j in all_fruits:
        if i == j:
            fruit_count += 1
    fruit_dict.append({'Fruit' : i, 'Count': fruit_count})
    fruit_count = 0

most = max(fruit_dict, key=lambda k:k['Count'])
least = min(fruit_dict, key=lambda k:k['Count'])
print('{} is the most liked fruit with {}'.format(most['Fruit'],most['Count']))
print('{} is the least liked fruit with {}'.format(least['Fruit'],least['Count']))

#total of unread messages
numbers =[]
for user in dataset:
    greeting = user['greeting']
    for word in greeting.split():
        if word.isdigit():
            numbers.append(int(word))
print('{} unread messages '.format(sum(numbers)))



    



    








    








    