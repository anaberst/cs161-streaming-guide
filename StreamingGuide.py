# Author: Anastasiya Berst
# GitHub username: anaberst
# Date: 12/05/2024 (uploaded to GitHub: 07/08/2025)
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

class StreamingService:
    """
    Represents a movie streaming service.
    """
    def __init__(self, name):
        """
        Initializes a streaming service object with two private data members:
        name and catalog.
        """
        self._name = name
        self._catalog = {} # empty dictionary for title (string): Movie (object) pairs.

    def get_name(self):
        """
        Returns the name of the streaming service.
        """
        return self._name

    def get_catalog(self):
        """
        Returns the streaming service catalog, a dictionary of Movie objects.
        """
        return self._catalog

class StreamingGuide:
    """
    Represents a movie streaming service guide.
    """
    def __init__(self):
        """
        Initializes a streaming guide object with one private data member:
        a streaming list.
        """
        self._streaming_list = [] # empty list for StreamingService objects

