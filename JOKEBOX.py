import json
import random
import os


jokes= [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "Why did the Python programmer wear glasses? Because he couldn't C.",
        "Why was the computer cold? It left its Windows open.",
        "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads."
    ],
favorites= []


1
if not os.path.exists('jokes.json'):
    with open('jokes.json', 'w') as f:
        json.dump(starter, f)

with open('jokes.json', 'r') as f:
    data = json.load(f)


class jokebox():
    def __init__(self, data):
        self.jokes = data["jokes"]
        self.favorites = data["favorites"]

    def tell(self):
        self.current = random.choice(self.jokes)
        print("\n", self.current)

    def add(self, new_joke):
        self.jokes.append(new_joke)
        print("joke added")

    def favorite(self):
        if self.current in self.favorites:
            print("already in favorites")
        else:
            self.favorites.append(self.current)
            print("saved to favorites")

    def show_favorites(self):
        if len(self.favorites) == 0:
            print("no favorites yet")
        else:
            print("\nYour favorite jokes :")
            for i, joke in enumerate(self.favorites, 1):
                print(i, "-", joke)

    def save(self):
        with open('jokes.json', 'w') as f:
            json.dump({"jokes": self.jokes, "favorites": self.favorites}, f)


JOKE = jokebox(data)


while True:
    try:
        option = int(input("enter option\n 1-TELL A JOKE\n 2-ADD A JOKE\n 3-SAVE LAST JOKE TO FAVORITES\n 4-SHOW FAVORITES\n 5-QUIT\n :"))
    except ValueError:
        print("Please enter a number from the options given")
        continue

    if option == 1:
        JOKE.tell()

    elif option == 2:
        new_joke = input("Type your joke :").strip()
        if new_joke != "":
            JOKE.add(new_joke)
            JOKE.save()
        else:
            print("nothing added")

    elif option == 3:
        if hasattr(JOKE, "current"):
            JOKE.favorite()
            JOKE.save()
        else:
            print("tell a joke first")

    elif option == 4:
        JOKE.show_favorites()

    elif option == 5:
        JOKE.save()
        print("Bye! Keep smiling")
        break

    else:
        print("option not valid")
