movies_watched = ["The Matrix", "Green Book", "Her"]
user_movie = input("Enter something you've watched recently: ")

if user_movie in movies_watched:
    print(f"i've watched {user_movie} too!")
else:
    print("I haven't watched that yet")
