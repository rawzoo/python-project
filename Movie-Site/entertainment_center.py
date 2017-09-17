import media
import fresh_tomatoes

simran = media.Movie("Simaran","A Gujarati housekeeping lady in the US allows ambition to get the better of her & gets involved in a world of crime","https://en.wikipedia.org/wiki/File:Simran_Poster.jpg","https://www.youtube.com/watch?v=_LUe4r6eeQA")

badshaho = media.Movie("Badshaho"," emergency era of the 1975-77.[7]","https://en.wikipedia.org/wiki/File:Ajay_Devgn%27s_Baadshaho.JPG","https://www.youtube.com/watch?v=Ny7fULat8ws")

dangal = media.Movie("Dangal","Women Wrestles With life","https://en.wikipedia.org/wiki/File:Dangal_Poster.jpg","https://youtu.be/jMfvlh0tjyo")
movies =["simran","badshaho","dangal"]



fresh_tomatoes.open_movies_page(movies)
#badshaho.movie_play()

