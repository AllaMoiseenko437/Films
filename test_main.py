import unittest
from main import MoviesLibrary

class TestMoviesLibrary(unittest.TestCase):

    def setUp(self):
        self.library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])

    def test_add_movie_to_horror(self):
        self.library.add_movie('Ужасы', 'Нечто')
        # Проверяем, что фильм 'Нечто' доступен в 'Ужасы'
        self.assertIn('Нечто', self.library.recommend('Ужасы'))

    def test_add_movie_to_comedy_and_check_horror(self):
        # Добавляем фильм в жанр 'Комедия'
        self.library.add_movie('Комедия', 'Весёлый питонист')
        # Проверяем, что фильм не добавился в 'Ужасы'
        self.assertNotIn('Весёлый питонист', self.library.recommend('Ужасы'))

    def test_add_movie_to_comedy_and_check_romance(self):
        # Добавляем фильм в жанр 'Комедия'
        self.library.add_movie('Комедия', 'Весёлый питонист')
        # Проверяем, что фильм не добавился в 'Романтика'
        self.assertNotIn('Весёлый питонист', self.library.recommend('Романтика'))

if __name__ == '__main__':
    unittest.main()