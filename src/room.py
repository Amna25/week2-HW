class Room:
    def __init__(self,name,capacity,entry_price):
        self.name =name
        self.capacity= capacity
        self.songs=[]
        self.guest=[]
        self.entry_price = 80

    def check_in_guest(self,guest):
        self.guest.append(guest)

    # def check_out_guest(self,guest):
    #     self.guest.remove(guest)

    # def enough_capacity(self):
    #     return self.capacity

    # def not_enough_capacity(self):
    #     if self.capacity >= len(self.room.guest):
    #         return 


    def favourite_song(self):
        return "Wohoo"
            
        