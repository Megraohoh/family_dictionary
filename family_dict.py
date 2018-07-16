# Define a dictionary that contains information about several members of your family. Use the following example as a template
my_family = {
    'sister': {
        'name': 'Brittany',
        'age': 36
    },
    'brother': {
        'name': 'Seth',
        'age': 24
    }
}
# How to set with a loop:
# family_siblings = set()
# for family_member, member_values in my_family.items():
#     family_siblings.add(f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old' )

# print("My family!", family_siblings)

# How to set with comprehension:
family_stuff = {
    f'{member_values["name"]} is my {family_member} and is {str(member_values["age"])} years old.'
    for (family_member, member_values) in my_family.items()
}

print("My family!", family_stuff)