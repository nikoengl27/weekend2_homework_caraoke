import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
   
    def setUp(self):
        self.room = Room("Special Room", 5)
        self.guest = Guest("George", 20, "Thunderstruck")
        self.playlist = []
    
    def test_guests_check_in(self):
        self.room.guests_check_in(Guest)
        self.assertEqual(3, self.room.guests_count())

    def test_guests_check_out(self):
        self.room.guests_check_out(Guest)
        self.assertEqual(1, self.room.guests_count())

    def test_add_song_to_room(self):
        self.room.add_song(Song)
        self.assertEqual(4, self.room.songs_count())

    def test_check_capacity(self):
        self.room.check_capacity
        self.assertEqual(2, self.room.guests_count())

    def test_enough_money(self):
        self.room.enough_money
        self.assertEqual(20, self.guest.wallet)

    def test_favourite_song(self):
        self.room.favourite_song
        self.assertEqual("Thunderstruck", self.guest.favourite_song)