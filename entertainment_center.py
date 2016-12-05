import fresh_tomatoes
import media

# adding movie details
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life","https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A story about blue people","https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")  

wolf_of_wall_street = media.Movie("Wolf of Wall Street", "A con salesman who becomes a multimillionaire but tricking people into buying penny stocks", "http://images.redbox.com/Images/EPC/Kiosk/6738.jpg", "https://www.youtube.com/watch?v=iszwuX1AK6A")

movies = [toy_story, avatar, wolf_of_wall_street]

# open movie page
fresh_tomatoes.open_movies_page(movies)
