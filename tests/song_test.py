import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
      self.song = Song("Signs", "Justin Timberlake")