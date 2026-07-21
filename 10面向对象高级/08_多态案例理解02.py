"""
    案例：多媒体播放鸭子类型示例
"""



class Mp3:
    def play(self):
        print("播放mp3音乐")

class Mp4:
    def play(self):
        print("播放Mp4视频")

class Flv:
    def play(self):
        print("播放Flv短视频")


def media_player(file):
    file.play()

media_player(Mp3())
media_player(Flv())
media_player(Mp4())
