import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Nick", 50, "Signs")
    
    