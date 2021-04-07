
#1
#You have rented some movies for your kids: The little mermaid (for 3 days), Brother Bear (for 5 days, they love it),
# and Hercules (1 day, you don't know yet if they're going to like it). 
# If price for a movie per day is 3 dollars, how much will you have to pay?
price_per_day = 3
the_little_mermaid = 3
brother_bear = 5
hercules = 1
result = price_per_day * (the_little_mermaid + brother_bear + hercules)
print('${}'.format(result))
print('------------------')


#2
# Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, 
# they pay you a different rate per hour. Google pays 400 dollars per hour
# Amazon 380, and Facebook 350. How much will you receive in payment for this week? 
# You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon.
dph_google = 400
dph_amazon = 380
dph_facebook = 350
google_hrs_worked = 6
facebook_hrs_worked = 10
amazon_hrs_worked = 4

result2 = (dph_google * google_hrs_worked) + (dph_amazon * amazon_hrs_worked) + (dph_facebook * facebook_hrs_worked)
print('${}'.format(result2))
print('------------------')


#3
#A student can be enrolled to a class only if 
# the class is not full and the class schedule 
# does not conflict with her current schedule.
max_credits = 12
Student1 = {'name':'Roger', 'credits': 4,  'schedule_conflicts': True}
Student2 = {'name':'David', 'credits': 12, 'schedule_conflicts': False}
Student3 = {'name':'Xavier', 'credits': 9, 'schedule_conflicts': False}

def enrolled(currentStudent):
    if(currentStudent['credits'] < max_credits and currentStudent['schedule_conflicts'] == False):
        print ('{} has been enrolled'.format(currentStudent['name']))
    else:
        print ('{} has not enrolled'.format(currentStudent['name']))


enrolled(Student1)
enrolled(Student2)
enrolled(Student3)
print('------------------')


#4 A product offer can be applied only if people buys more than 2 items, 
# and the offer has not expired. Premium 
# members do not need to buy a specific amount of products.
product_offer_after_this_purchase_amount = 2
Customer1 = {'name':'Roger', 'items_purchased': 4, 'expired': False, 'premium_member': False}
Customer2 = {'name':'David', 'items_purchased': 2, 'expired': False, 'premium_member': False}
Customer3 = {'name':'Xavier','items_purchased': 1, 'expired': False, 'premium_member': True}

def qualify(currentCustomer):
    if((currentCustomer['items_purchased'] > product_offer_after_this_purchase_amount 
        and currentCustomer['expired'] == False) or currentCustomer['premium_member'] == True):
        print ('{} has qualified for product offer'.format(currentCustomer['name']))
    else:
        print ('{} has not qualified for product offer'.format(currentCustomer['name']))


qualify(Customer1)
qualify(Customer2)
qualify(Customer3)
print('------------------')

#5  Create a variable that holds a boolean value for each of the following conditions:
# the password must be at least 5 characters
# the username must be no more than 20 characters
# the password must not be the same as the username
# bonus neither the username or password can start or end with whitespace


password_min_length = 5
username_max_length = 20
invalidCharacters = [' ']

currentUser1 = {'username':'codeup', 'password': 'notastrongpassword'}
currentUser2 = {'username':'codeup', 'password': 'codeup'}
currentUser3 = {'username':'codeupjhbguguyguyguyguygcniubhuinub', 'password': 'codeup'}
currentUser4 = {'username':' codeup ', 'password': 'codeup'}

def validate(currentUser):
    if(len(currentUser['password']) < password_min_length):
        print('password too short')
        return False
    if (len(currentUser['username']) > username_max_length):
        print('username too long')
        return False
    if (currentUser['username'] == currentUser['password']):
        print('password and username cannot be the same')
        return False
    if(invalidCharacters[0]  in currentUser['username']):
        print('white space in username detected')
        return False
    else:
        print('Succcess!')
        return True

validate(currentUser1)
validate(currentUser2)
validate(currentUser3)
validate(currentUser4)








