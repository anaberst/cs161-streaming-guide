# Author: Anastasiya Berst
# GitHub username: anaberst
# Date: 12/05/2024
# Description:
    # This program contains three classes:
        ## Movie, representing a movie.
        ## StreamingService, representing a movie streaming platform.
        ## StreamingGuide, representing a guide for finding a specific movie.
    # StreamingGuide contains a list of StreamingService objects.
    # StreamingService contains a dictionary of Movie objects.

class Movie:
    """
    Represents an individual movie.
    """
    def __init__(self, title, genre, director, year):
        """
        Initializes a movie object with four private data members:
        title, genre, director, and release year.
        """
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """
        Returns the movie's title.
        """
        return self._title

    def get_genre(self):
        """
        Returns the movie's genre.
        """
        return self._genre

    def get_director(self):
        """
        Returns the movie's director.
        """
        return self._director

    def get_year(self):
        """
        Returns the movie's release year.
        """
        return self._year

















