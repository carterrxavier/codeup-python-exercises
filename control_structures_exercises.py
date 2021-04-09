#1
weekend = ['SATURDAY', 'SUNDAY']

dayofweek = input('Day of the week: ')
if dayofweek.upper() == "MONDAY":
    print('It is monday')
else: 
    print('It is not monday')

dayofweek = input('Day of the week: ')

if dayofweek.upper() in weekend:
    print('Its the weekend')
else:
    print('Its not the weekend')

#calculate weekly check


hours_in_normal_week = 40
hours_worked_in_week = float(input('How many hours worked?  '))
hourly_rate = float(input('whats your hourly rate: '))
if(hours_worked_in_week > hours_in_normal_week):
    time_half = 1.5
    overtime = (hours_worked_in_week - hours_in_normal_week) * (time_half * hourly_rate)
    weekly_check = (hours_in_normal_week * hourly_rate) + overtime
else:
    weekly_check = (hours_worked_in_week * hourly_rate)
print('${}'.format(weekly_check))


#2
i = 4
while i:
    if i < 15:
        i += 1
        print(i)
    else: 
        break
print()

i = 2
print(i)
while i:
    if i < 100:
        i += 2
        print(i)
    else:
        break


i = 100
print(i)
while i > -10:
        i = i - 5
        print(i)


i = 2
while i < 10000000:
    print(i)
    i = i*i


i = 100
print(i)
while i > 5:
    i = i - 5
    print(i)


num = int(input('Pick a number: '))
for number  in range(1, 11):
    print('{} X {} = {}'.format(num, number , num * number))


for num in range (1,10):
    print(str(num) * num)



    
userInput = int(input('Number to skip is: '))
while (userInput % 2 == 0 and userInput > 50) not userInput.isdigit():
    userInput = int(input('Number to skip is: '))

for num in range(1, 50, 2):
    if(num != userInput):
        print('Here is an odd number: {}'.format(num))
    else:
        print('Yikes! skipping number: {}'.format(userInput))


userInput = int(input('Enter a positive number: '))
while userInput <= 0:
    userInput = int(input('Enter a positive number: '))

for num in range(0, userInput + 1):
    print(num)


for num in range(1, 101):
    if(num % 3 == 0):
        print('fizz')
    elif(num % 5 == 0):
        print('Buzz')
    else:
        print(num)




while True:
    num = input('Please insert a postive interger: ')
    if num.isdigit():
        if int(num) >0:
            break
proceed = input('continue?')
if proceed.lower().startswith('y'):
    num = int(num)
    print('number | squared | cubed ')
    print('------ | ------- | ------')
    for number in range(1, num + 1):
        i_squared = number ** 2
        i_three = number ** 3
        print('  {}    |   {}      |     {}     '.format(number, i_squared, i_three))




           
    




        











