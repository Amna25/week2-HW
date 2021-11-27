import unittest
from src.song import Song
class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Best day","happy song")

    def test_song_has_name(self):
        self.assertEqual("Best day", self.song.name)

    def test_song_has_type(self):
        self.assertEqual("happy song", self.song.type)