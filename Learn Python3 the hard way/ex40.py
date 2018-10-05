class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
# how did the object goes to lyrics???这参数不同名啊 怎么传递过去的？
# 答：__init__函数会自动接收实例化时的参数，可以使多个。
happy_baby = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_baby.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
