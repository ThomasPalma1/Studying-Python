print("==========")
print(5 == 5)
print(5 > 5)
print(10 != 10)
print("==========")

# comparison: ==, !=, >, <, >=, <=

friends = ["Elliot", "Walter"]
abroad = friends  # ["Elliot", "Walter"]

print(friends == abroad)
print(friends is abroad)

# == is for value equality.
# it's used to know if two objects have the same value.
# "is" is for reference equality.
# it's used to know if two references refer (or point) to the same object, i.e if they're identical.
