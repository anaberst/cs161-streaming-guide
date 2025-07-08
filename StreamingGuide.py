# Author: Anastasiya Berst
# GitHub username: anaberst
# Date: 12/05/2024 (uploaded to GitHub: 07/08/2025)
# Description:
    # This program contains three classes:
        ## Movie, representing a movie
        ## StreamingService, representing a movie streaming platform
        ## StreamingGuide, representing a guide for finding a specific movie
    # StreamingGuide contains a list of StreamingService objects
    # StreamingService contains a dictionary of Movie objects

class Movie:
    """
    Represents an individual movie
    """
    def __init__(self, title, genre, director, year):
        """
        Initializes a movie object with four private data members:
        title, genre, director, and release year
        """
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """
        Returns the movie's title
        """
        return self._title

    def get_genre(self):
        """
        Returns the movie's genre
        """
        return self._genre

    def get_director(self):
        """
        Returns the movie's director
        """
        return self._director

    def get_year(self):
        """
        Returns the movie's release year
        """
        return self._year

class StreamingService:
    """
    Represents a movie streaming service
    """
    def __init__(self, name):
        """
        Initializes a streaming service object with two private data members:
        name and catalog
        """
        self._name = name
        self._catalog = {} # empty dictionary for title (string): Movie (object) pairs

    def get_name(self):
        """
        Returns the name of the streaming service
        """
        return self._name

    def get_catalog(self):
        """
        Returns the streaming service catalog, a dictionary of Movie objects
        """
        return self._catalog

    def add_movie(self, movie_object):
        """
        Receives a Movie object to add to the streaming service catalog
        """
        self._catalog[movie_object.get_title()] = movie_object  # title (string): movie (object) pair

    def delete_movie(self, movie_title):
        """
        Receives a Movie object to delete from the streaming service catalog
        [Assumption: there are no duplicate movies]
        """
        if movie_title in self._catalog:
            del self._catalog[movie_title]

class StreamingGuide:
    """
    Represents a movie streaming service guide
    """
    def __init__(self):
        """
        Initializes a streaming guide object with one private data member:
        a streaming list
        """
        self._streaming_list = [] # empty list for StreamingService objects

    def add_streaming_service(self, stream_service_object):
        """
        Receives a StreamingService object to add to the streaming guide
        """
        self._streaming_list.append(stream_service_object)

    def delete_streaming_service(self, stream_service_name):
        """
        Receives the name of a streaming service to remove from the guide
        [Assumption: all streaming services have unique names]
        """
        for service in self._streaming_list:
            if stream_service_name == service.get_name():
                self._streaming_list.remove(service)

    def who_streams_this_movie(self, movie_title):
        """
        Receives a movie title and returns either a dictionary of movie info or None if unavailable
        """
        stream_info_dict = {} # empty dictionary for movie info: title, year, streaming services
        stream_services_list = [] # empty list for services streaming the movie

        for service in self._streaming_list: # iterate over streaming guide
            if movie_title in service.get_catalog(): # check if movie offered

                stream_services_list.append(service.get_name())
                stream_info_dict['title'] = movie_title
                stream_info_dict['year'] = int(service.get_catalog()[movie_title].get_year())
                stream_info_dict['services'] = stream_services_list

        if len(stream_services_list) > 0:
            return stream_info_dict
        else:
            return None



