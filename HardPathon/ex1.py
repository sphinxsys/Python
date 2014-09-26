#Basic Exceises
print("Hello World!")
#print("I'd much rather you 'not'.")
print('I "said" do not touch this.')

print(3+2)

cars = "100"
print("There are", cars, "cars available.")

my_name = "Zed A. Shaw"
my_age = 35.0  # not  a lie

print("Let's talk about %r. He's %d years old." % (my_name, my_age))

x = "There are %d types of people." % 10
print(x)
print("I said: %r." % x)

print("."*10)

formatter = "%r %r %r %r"
print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (formatter, formatter, formatter, formatter % (1, 2, 3, formatter)))

months = "Jan\nFeb\nMar\nApr\nMay\nJun\nAug"
print("Here are the months: ", months)

print('''There's something going on here.''')