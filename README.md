# :movie_camera: CS161 Streaming Guide
Final project for `CS161: Introduction to Computer Science I` at Oregon State University. It has been approved for public sharing.

This project simulates a movie streaming guide that allows users to:

- Add and remove movies from streaming service catalogs
- Manage multiple streaming platforms
- Search for where a specific movie is available to stream

It consists of three main classes:

- `Movie`: Represents a movie with attributes title, genre, director, and release year
- `StreamingService`: Represents a platform (e.g., Netflix, Hulu) with a catalog of available movies
- `StreamingGuide`: A central guide that tracks all streaming services and can find which services stream a select movie

The project demonstrates class-based design, object composition, and encapsulation using private attributes and getter methods.

## :hourglass_flowing_sand: Testing

The file `test_streaming_guide.py` includes unit tests that cover:

- Creating and accessing movie data
- Adding/removing movies from a streaming service
- Managing multiple streaming services
- Searching for a movie across all services

## :open_file_folder: File Structure
```
cs161-streaming-guide/
├── README.md                 # You are here
├── streaming_guide.py        # Main class definitions
└── test_streaming_guide.py   # Unit tests for the project  
```
