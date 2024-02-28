class MixinLog:
    def __init__(self, *args, **kwargs):
        print(repr(self))

    def __repr__(self):
        print(f'{__class__.__name__}({self.__dict__.items()})')
