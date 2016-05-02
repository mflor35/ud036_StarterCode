import media
import fresh_tomatoes

# Movies available in the entertainment center
list_movies = [media.Movie("Toy Story",
                           "The toys come alive!",
                           "http://vignette4.wikia.nocookie.net/pixar/images/c/ca/Toy_story_ver1_xlg.jpg/revision/latest?cb=2011051142143",  # noqa
                           "https://www.youtube.com/watch?v=KYz2wyBy3kc"),
               media.Movie("Avatar",
                           "Chick flick in an alien planet",
                           "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",  # noqa
                           "https://www.youtube.com/watch?v=5PSNL1qE6VY"),
               media.Movie("Kung Fu Panda",
                           "Jackie-chan-like Panda",
                           "http://ia.media-imdb.com/images/M/MV5BMTIxOTY1NjUyN15BMl5BanBnXkFtZTcwMjMxMDk1MQ@@._V1_UY1200_CR69,0,630,1200_AL_.jpg",  # noqa
                           "https://www.youtube.com/watch?v=PXi3Mv6KMzY"),
               media.Movie("I, Robot",
                           "Robots and AI take over the world",
                           "https://upload.wikimedia.org/wikipedia/en/3/3b/Movie_poster_i_robot.jpg",  # noqa
                           "https://www.youtube.com/watch?v=rL6RRIOZyCM"),
               media.Movie("Chappie",
                           "Robots does have counciousness",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcRyiMieeP976GMk_zLPnMiqZWuNFLKs4YHbV-22o7rsK16-ufUZ",  # noqa
                           "https://www.youtube.com/watch?v=lyy7y0QOK-0"),
               media.Movie("Mr. Nobody",
                           "Whao!",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcQ9hWxJsCyiWB894QDiPJEYqZf4RVJbKBOZ1k7r6XrSNOvVD3XK",  # noqa
                           "https://www.youtube.com/watch?v=mpi0qsp3v_w")]

# Display all the available movies in the entertainment center
fresh_tomatoes.open_movies_page(list_movies)
