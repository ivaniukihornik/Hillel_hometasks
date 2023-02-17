# 6
# You have a group of people with non-unique names. Generate a list of non-duplicate names
# (you cannot use set for this task.
# If there are 2 johns in the list, you need to take only one of them.
# "John Dow", "John Dow", "Marta Dow" => "John Dow", "Marta Dow ")

people = ['John Dow', 'John Dow', 'Marta Dow', 'Marta Dow', 'Anny Lee', 'Marta Dow']
unique = []

for person in people:
    if person not in unique:
        unique.append(person)

print(unique)
