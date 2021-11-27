class Guest:
    def __init__(self,name,wallet):
        self.name =name
        self.wallet = wallet
        self.favourite_song= []

    def add_song(self,song):
        self.favourite_song.append(song)

    def enough_money(self):
        return self.wallet
    
