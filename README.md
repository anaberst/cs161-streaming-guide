# :movie_camera: Streaming Guide
A Python program that models a system for organizing movies across different streaming services using object-oriented programming (OOP) principles.

## :one: Project Overview
This project simulates a streaming guide that lets users manage a collection of streaming services and the movies they offer. It includes three main classes:

- `Movie`: represents an individual movie with attributes like title, genre, director, and year.
- `StreamingService`: represents a streaming platform that holds a catalog of `Movie` objects.
- `StreamingGuide`: manages multiple `StreamingService` instances and can search for where a specific movie is available.

The program demonstrates foundational OOP concepts including encapsulation, object relationships, and nested data structures (e.g. a guide contains services, and services contain movies).

## :two: Learning Goals
This project was developed for `CS161`, an introductory Python programming course at Oregon State University. Key concepts practiced include:

- Defining and using classes and objects
- Encapsulation using private data members
- Managing relationships between objects
- Implementing search logic over nested data structures

## :three: How to Run

No special setup is required.

1. Ensure you have Python 3 installed.
2. Save your code in a file named `StreamingGuide.py`.
3. Run your script or use the sample code snippet below to test functionality:

```python
from StreamingGuide import Movie, StreamingService, StreamingGuide

movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)

netflix = StreamingService('Netflick')
netflix.add_movie(movie_2)

guide = StreamingGuide()
guide.add_streaming_service(netflix)

results = guide.who_streams_this_movie('Home Alone')
print(results)
