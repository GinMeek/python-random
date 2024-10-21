import random

def get_and_remove(collection):
    selection = random.choice(collection)
    collection.remove(selection)
    return selection

students = ['other', 'student1', 'me', 'student2', 'me', 'other']
groups = {
    'group1': [],
    'group2': [],
    'group3': [],
    'group4': [],
    'group5': []
}

while len(students) > 0:
    for key in groups.keys():
        if len(students) > 0:
            groups[key].append(get_and_remove(students))

for group, members in groups.items():
    print(f'{group}: {members}')
