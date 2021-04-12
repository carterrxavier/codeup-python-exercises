#1 Define a function named is_two. 
# It should accept one input and return 
# True if the passed input is either the number or the string 2, False otherwise.
def is_two(one_input):
    if one_input in [2, '2'] :
        return True
    else: 
        return False

#2
#Define a function named is_vowel. 
# It should return True if the passed string is a vowel, False otherwise
def is_vowel(vowel):
    if vowel.upper() in ['A', 'E', 'I', 'O', 'U']:
        return True
    else:
        return False

#3 Define a function named is_consonant.
#  It should return True if the passed string is a consonant,
#  False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(consonant):
    if consonant.upper() not in ['A', 'E', 'I', 'O', 'U']:
        return True
    else:
        return False

#4 Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.
def cap_if_const(word):
   if word[0].upper() not in ['A', 'E', 'I', 'O', 'U']:
       return word.title()
   else:
       return word

#5 Define a function named calculate_tip. 
# It should accept a tip percentage
#  (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(percent, total):
    if percent >=0 and percent <=1:
        return round((percent * total) + total, 2)

#6 Define a function named apply_discount. 
# It should accept a original price, and a discount percentage,
#  and return the price after the discount is applied.
def apply_discount(total, percentage_off):
    if percentage_off >= 0 or percentage_off <= 1:
         return round(total - (total * percentage_off), 2)


# 7 Define a function named handle_commas.
#  It should accept a string that is a number that 
# contains commas in it as input, and return a number as output.
def handle_commas(phrase):
   return int(phrase.replace(',',''))

#8 Define a function named get_letter_grade. 
# It should accept a number and return the letter grade 
# associated with that number (A-F).
def get_letter_grade(grade):
    if grade <= 100 and grade >= 90:
        return 'A'
    elif grade < 90 and grade >= 80:
        return 'B'
    elif grade < 80 and grade >= 70:
        return 'C'
    elif grade <= 70 and grade >= 60:
        return 'D'
    else:
        return 'F'

#9 define a function named remove_vowels that 
# accepts a string and returns a string with all the vowels removed.
def remove_vowels(phrase):
    vowels = ('a', 'e', 'i','o','u')
    for char in phrase.lower():
        if char in vowels:
            phrase = phrase.replace(char, '')
    return phrase

#10 Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name First Name will become first_name % Completed will become completed
def normalize_name(string_name):
    for char in string_name:
        if not char.isalpha:
            string_name = string_name.replace(char,'')
        if char == " ":
            string_name = string_name.replace(char, '_')
    if string_name[0]  == '_':
            string_name = string_name.replace(char, )
    return(string_name.lower())



#11 Write a function named cumulative_sum 
# that accepts a list of numbers and returns
#  a list that is the cumulative sum of the numbers in the list.
def cumulative_sum(num_list):
    newlist = []
    temp = 0
    for i in range(0, len(num_list)):
        temp+=num_list[i]
        newlist.append(temp)
    return newlist

x = cumulative_sum([10,20,30])
print(x)


#bonus 
# #1 Create a function named twelveto24. 
# It should accept a string in the format 10:45am or 4:30pm 
# and return a string that is the representation of the time in a 24-hour format. 
# Bonus write a function that does the opposite.
def twelveto24(time):
    if 'am' in time:
        time = time.replace('am','')
    elif 'pm' in time:
        time = time.replace('pm','')
        first_digits = time.split(':')
        first_plus_12 = int(first_digits[0]) + 12
        time = time.replace(str(first_digits[0]), str(first_plus_12))
    return(time)

        
    
      
x = twelveto24('2:30pm')
print(x)

        
    










        

















