# guest list
guests = ['mozart', 'ghandi', 'franco']

# dinner message
dinnermsg = "you are cordially invited to dinner."

# print each guest a dinner message
print(f"Mr. {guests[0].title()}, {dinnermsg}")
print(f"Mr. {guests[1].title()}, {dinnermsg}")
print(f"Mr. {guests[2].title()}, {dinnermsg}")

print()
# how many are coming?
print(f"There are {len(guests)} guests coming to dinner.")