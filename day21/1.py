
class Animal:
    def __init__(self):
        self.n_eyes = 2

    def breathe(self):
        print("inhale.. exhale..")


class fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Underwater")
    def bark(self):
        print("Bhau.. bhau")


tom = fish()
tom.breathe()