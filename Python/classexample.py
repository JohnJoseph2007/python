class Friends:
    def __init__(self, stupidlevel, howdumb, howfar, howbuddha, name):
        self.st = stupidlevel
        self.hd = howdumb
        self.hf = howfar
        self.hb = howbuddha
        self.name = name

    def SayHi(self):
        print(f"Hi, {self.name}")

swayam = Friends(6, 11, 8, 14, "Swayam")
swayam.SayHi()
print(swayam.hb)