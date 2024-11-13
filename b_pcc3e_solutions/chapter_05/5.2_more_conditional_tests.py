# testing for equality
string = "Mr. Salas"
print("Is the teacher for Technology class Mr. Salas?")
print(string == "Mr. Salas")

# inequality
string2 = "Mr. Tolliver"
print("Is the teacher for Communications class Mr. Salas?")
print(string2 != "Mr. Tolliver")

# using the lower method
auto = "BMW"
auto == "bmw" # this returns false
auto.lower() == "bmw"
# making it false
auto = "Mercedes"
auto.lower() == "BMW"

# numerical tests

# equal false
grade = 93
print("Is 90 equal to 93?")
print(grade == 90)

# equal true
grade = 97
print("Is 97 equal to 97?")
print(grade == 97)

# inequality false
grade = 88
print("Is 88 not equal to 88?")
print(grade != 88)

# inequality true
grade = 88
print("Is 88 not equal to 89?")
print(grade != 89)

# greater than or equal true
grade = 99
print("Is 99 greater than or equal to 100?")
print(grade >= 100)

# less than or equal false
grade = 99
print("Is 99 less than or equal to 100?")
print(grade <= 100)

# greater than true
grade = 50
print("Is 50 greater than 0?")
print(grade > 0)

# less than true
grade = 60
print("Is 60 less than 70?")
print(grade < 70)

# greater than, using an if loop
grade = 73
if grade > 60:
  print("I barely passed that test, didn't I?")
# this will print, because the check is True

print()

# using AND, both conditions have to be true
grade_1 = 87
grade_2 = 93
print("Did both of you pass the test?")
print(grade_1 > 60 and grade_2 > 60)

# using OR, only one of the conditions need to be true
grade_1 = 87
grade_2 = 50
print("Did at least one of you pass the test?")
print(grade_1 > 60 or grade_2 > 60)

# test if an item is in the list
# use IN
mylist = ['nike', 'puma', 'reebok']
# first time is true
print("Is Nike one of our vendors?")
print('nike' in mylist)
# second time is false
print("Is Adidas one of our vendors?")
print('adidas' in mylist)

# using NOT and IF to check if something is in a list
mylist = ['nike', 'puma', 'reebok']
vendor = 'adidas'
if vendor not in mylist:
  print(f"{vendor.title()} is not one of our vendors.")


# more involved example using a list
students = ['kanner', 'brock', 'charlie', 'charles', 'derek', 'london', 'olivia']

# print the list of students
print("These students are in Technology class:")
for student in students:
    print(student.title())

print()

# evaluate to True by checking the list of students
print("Is Brock in class today?")
user = 'brock'
if user in students:
    print(f"{user.title()} is not in class today!")