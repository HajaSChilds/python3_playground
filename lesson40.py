class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])  

bulls_on_parade = Song(["They rally around tha family", 
                        "With pockets full of shells"])

ring_around_the_rosie = Song([" Ring around the rosie",
                               "a pocket full of posies",
                               "ashes, ashes they all fall down"])
                               


santa = ["We wish you a merry christmas" ]                                                     

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

ring_around_the_rosie.sing_me_a_song()

merry_christmas = Song([santa])

merry_christmas.sing_me_a_song()
