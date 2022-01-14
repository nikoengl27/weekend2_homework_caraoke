from classes.guest import Guest
from classes.song import Song

class Room:

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost
        self.guestlist = [Guest, Guest]
        self.playlist = [Song, Song, Song]

    def guests_count(self):
        return len(self.guestlist)
    
    def guests_check_in(self, guest):
        self.guestlist.append(guest)

    def guests_check_out(self,guest):
        self.guestlist.remove(guest)
        
    def songs_count(self):
        return len(self.playlist)
    
    def add_song(self, song):
        self.playlist.append(song)
   
    def check_capacity(self, amount):
         if self.guests_count > amount:
            return "no more peoples"

    def enough_money(self):
        if self.guest.wallet < self.cost:
            return "Not enough moneys"

    def favourite_song(self):
        if self.guest.favourite_song in self.playlist:
            return "Whoo!"



 
    