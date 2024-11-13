pizzas = ['cheese', 'pepperoni', 'sausage', 'mushroom', 'meatball', 'supreme', 'white', 'veggie', 'primavera']
print(pizzas)
for pizza in sorted(pizzas):
    print(pizza)
print(len(pizzas))

print()

print("The first three items in the list are:")
# just print the slice from the list
# print(pizzas[0:3])
# using a loop
for pizza in pizzas[0:3]:
    print(pizza.title())

print()

print("Three items from the middle of the list are:")
for pizza in pizzas[3:6]:
    print(pizza.title())

print()

print("The last three items in the list are:")
for pizza in pizzas[-3:]:
    print(pizza.title())