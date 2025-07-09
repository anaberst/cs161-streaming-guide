# Author: Anastasiya Berst
# GitHub username: anaberst
# Date: 12/05/2024 (uploaded to GitHub: 07/08/2025)
# Description:
    # This program contains unit tests for streaming_guide.py

import unittest
from streaming_guide import Movie, StreamingService, StreamingGuide

class TestStreamingGuide(unittest.TestCase):

    def setUp(self):
        # Create Movie objects
        self.movie_1 = Movie('The Seventh Seal', 'comedy', 'Ingmar Bergman', 1957)
        self.movie_2 = Movie('Home Alone', 'tragedy', 'Chris Columbus', 1990)
        self.movie_3 = Movie('Little Women', 'action thriller', 'Greta Gerwig', 2019)
        self.movie_4 = Movie('Galaxy Quest', 'historical documents', 'Dean Parisot', 1999)

        # Create StreamingService objects
        self.stream_serv_1 = StreamingService('Netflick')
        self.stream_serv_1.add_movie(self.movie_2)
        self.stream_serv_1.add_movie(self.movie_3)

        self.stream_serv_2 = StreamingService('Hula')
        self.stream_serv_2.add_movie(self.movie_4)
        self.stream_serv_2.add_movie(self.movie_2)
        self.stream_serv_2.add_movie(self.movie_3)

        self.stream_serv_3 = StreamingService('Dizzy+')
        self.stream_serv_3.add_movie(self.movie_4)
        self.stream_serv_3.add_movie(self.movie_3)
        self.stream_serv_3.add_movie(self.movie_1)

        # Create StreamingGuide and add services
        self.guide = StreamingGuide()
        self.guide.add_streaming_service(self.stream_serv_1)
        self.guide.add_streaming_service(self.stream_serv_2)
        self.guide.add_streaming_service(self.stream_serv_3)

    def test_who_streams_galaxy_quest(self):
        expected = {
            'title': 'Galaxy Quest',
            'year': 1999,
            'services': ['Hula', 'Dizzy+']
        }
        result = self.guide.who_streams_this_movie('Galaxy Quest')
        self.assertEqual(result, expected)

    def test_who_streams_the_seventh_seal(self):
        expected = {
            'title': 'The Seventh Seal',
            'year': 1957,
            'services': ['Dizzy+']
        }
        result = self.guide.who_streams_this_movie('The Seventh Seal')
        self.assertEqual(result, expected)

    def test_who_streams_little_women_all_services(self):
        expected = {
            'title': 'Little Women',
            'year': 2019,
            'services': ['Netflick', 'Hula', 'Dizzy+']
        }
        result = self.guide.who_streams_this_movie('Little Women')
        self.assertEqual(result, expected)

    def test_streaming_service_deletion(self):
        self.guide.delete_streaming_service('Hula')
        expected = {
            'title': 'Little Women',
            'year': 2019,
            'services': ['Netflick', 'Dizzy+']
        }
        result = self.guide.who_streams_this_movie('Little Women')
        self.assertEqual(result, expected)

        self.guide.delete_streaming_service('Netflick')
        expected = {
            'title': 'Little Women',
            'year': 2019,
            'services': ['Dizzy+']
        }
        result = self.guide.who_streams_this_movie('Little Women')
        self.assertEqual(result, expected)

    def test_movie_deletion(self):
        self.stream_serv_3.delete_movie('Little Women')
        self.guide.delete_streaming_service('Hula')
        self.guide.delete_streaming_service('Netflick')
        result = self.guide.who_streams_this_movie('Little Women')
        self.assertIsNone(result)

    def test_movie_not_found(self):
        result = self.guide.who_streams_this_movie('Mak')
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
