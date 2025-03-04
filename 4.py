"""
my_name = "Nikita"
my_surname = "Bevziuk"
my_age = 18

name = "Mark"
surname = "Denisov"
age = 27

text = "My name %s, I'm %d, and this %s, he's %d. We bought tickets under the names %s and %s."

print("Age difference: ",  abs(my_age-age))                       # part 1
print("Number of letters in names: ", len(my_name)+len(name))     # part 2
print(text %(my_name, my_age, name, age, my_surname, surname))    #part 3
"""