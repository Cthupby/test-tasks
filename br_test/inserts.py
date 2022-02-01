from base import Session, engine, Base
from client_movie import Client, Movie


# 1 - generate database schema
Base.metadata.create_all(engine)

# 2 - create a new session
session = Session()

# 4 - create movies
back_to_future = Movie("Back to the Future", "sci-fi | comedy",  1985, "USA")
heart_of_dog = Movie("Heart of a Dog", "drama | sci-fi", 1988, "USSR")
the_matrix = Movie("The Matrix", "sci-fi", 1931, "USA")
gentlemen_of_fortune = Movie("Gentlemen of Fortune", "comedy", 1971, "USSR")
home_alone = Movie("Home alone", "comedy", 1990, "USA")
alien = Movie("Alien", "horror | sci-fi", 1979, "USA")
city_lights = Movie("City Lights", "comedy", 1931, "USA")
kin_dza_dza = Movie("Kin-dza-dza!", "sci-fi | comedy", 1986, "USSR")
bladerunner = Movie("Bladerunner", "sci-fi | drama", 1981, "USA")
twelve_chairs = Movie("Twelve Chairs", "comedy", 1971, "USSR")

# 5 - creates clients
alex_d = Client("Alex Dverev", 44)
georg_h = Client("Georg Huhaev", 37)
mark_l = Client("Mark Liliev", 21)
kirk_titov = Client("Kirk Titov", 29)
anton_rutin = Client("Anton Rutin", 41)
kirill_letov = Client("Kirill Letov", 33)

# 6 - add actors to movies
alex_d.movies = [back_to_future, alien, kin_dza_dza, the_matrix]
georg_h.movies = [gentlemen_of_fortune, heart_of_dog, back_to_future]
mark_l.movies = [home_alone, city_lights, gentlemen_of_fortune]
kirk_titov.movies = [the_matrix, alien, kin_dza_dza, bladerunner]
anton_rutin.movies = [back_to_future, the_matrix, kin_dza_dza, twelve_chairs]
kirill_letov.movies = [city_lights, home_alone, heart_of_dog, twelve_chairs]

# 9 - persists data
session.add(alex_d)
session.add(georg_h)
session.add(mark_l)
session.add(kirk_titov)
session.add(anton_rutin)
session.add(kirill_letov)

# 10 - commit and close session
session.commit()
session.close()
