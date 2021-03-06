# Incomplete app!
import pprint

MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "
movies = []

# You may want to create a function for this code
def movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })
# Create other functions for:
#   - listing movies

def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")

def listar():
    if len(movies) != 0:
        for movie in movies:
            print_movie(movie)
    else:
        print("No hay datos en el array de movies")
#   - finding movies
def buscar():
    title1 = input("Enter the movie title: ")
    for movie in movies:
        if movie["title"] == title1:
            print_movie(movie)
# And another function here for the user menu
selection = input(MENU_PROMPT)
while selection != 'q':
    if selection == "a":
        movie()
    elif selection == "l":
        listar()
    elif selection == "f":
        buscar()
    else:
        print('Unknown command. Please try again.')

    selection = input(MENU_PROMPT)


# Remember to run the user menu function at the end!