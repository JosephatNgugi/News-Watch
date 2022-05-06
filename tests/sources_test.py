import unittest
from app.models import Sources


class SourcesTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Sources class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_source = Sources(
            "bbc-news",
            "BBC News",
            "https://www.now.then.org",
            "Sports",
            "US",
            "english"
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))

    def test_init(self):
        """
        test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_movie.id, "bbc-news")
        self.assertEqual(self.new_movie.name, "BBC News")
        self.assertEqual(self.new_movie.url, "https://www.now.then.org")
        self.assertEqual(self.new_movie.category, "Sports")
        self.assertEqual(self.new_movie.country, "US")
        self.assertEqual(self.new_movie.language, "english")

