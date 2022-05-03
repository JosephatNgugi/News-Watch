import unittest
from app.models import News


class NewsTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the News class
    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_news = News(
            "null",
            "News Today",
            "Joe J",
            "What Happened",
            "Whatever happened happened, what is there to say about it",
            "https://www.now.then.org",
            "https:image.this/1235/net.com",
            "12:40:45",
            "After the unthinkable happened, there wasn't much to think about apart from being mesmrized and begin reminescing on the thought that were left on the peoples minds......."
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

    def test_init(self):
        """
        test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_movie.id, "null")
        self.assertEqual(self.new_movie.name, "News Today")
        self.assertEqual(self.new_movie.author, "Joe J")
        self.assertEqual(self.new_movie.title, "What Happened")
        self.assertEqual(self.new_movie.description, "Whatever happened happened, what is there to say about it")
        self.assertEqual(self.new_movie.url, "https://www.now.then.org")
        self.assertEqual(self.new_movie.urlToImage, "https:image.this/1235/net.com")
        self.assertEqual(self.new_movie.urlToImage, "12:40:45")
        self.assertEqual(self.new_movie.urlToImage, "After the unthinkable happened, there wasn't much to think about apart from being mesmrized and begin reminescing on the thought that were left on the peoples minds.......            ")


