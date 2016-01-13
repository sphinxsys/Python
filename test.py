bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

# basic statements
print(bob[0])
print(sue[2])
print(bob[0].split()[-1])

people = [bob, sue]
for person in people:
    print(person[0].split()[-1])
    person[2] *= 1.20

pays = [person[2] for person in people]
print(pays)

pays = map((lambda x: x[2]), people)
print(list(pays))