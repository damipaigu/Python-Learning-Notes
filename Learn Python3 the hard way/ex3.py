my_name = 'Jianbin LIU'
my_age = 28 # not a lie
my_height = 1.87 # meter
my_weight = 84.5 # kg
my_bmi = round(my_weight / my_height ** 2, 1)
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} cm tall.")
print(f"He's {my_weight} kg heavy.")
print(f"His BMI is {my_bmi}.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I had {my_age}, {my_height}, and {my_weight} I get {total}.")
