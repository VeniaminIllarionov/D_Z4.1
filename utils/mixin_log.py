class MixinLog:
    def __init__(self, *args, **kwargs):
        """Вписываем в инициализатор метод repr"""
        print(repr(self))

    def __repr__(self):
        '''Method repr для вывода в инициализаторе сообщения в виде сзданного класа и его атрибутов(свойств)'''
        return f'{self.__class__.__name__}({self.__dict__.items()})'
