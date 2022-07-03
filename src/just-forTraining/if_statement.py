day_of_week = input("What day of week is it today? ").lower()

# the lower() method returns a string where all characters are lower case.

if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "tuesday":
    print("it's still tuesday!")
else:
    print("Your week hasn't started yet")

# python is indent sensitive like yaml
# make sure that everything is always very well indented
# so that there is no problem


# the order of keywords is important, remember that;
# the "if" comes first, then any "elif", if you want them, and finally the "else";
# the "elif" and "else" keywords are optional if you want to add those branches to your "if statement".
