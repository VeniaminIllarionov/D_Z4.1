class MixinLog:
    def __init__(self, *args, **kwargs):
        """Вписываем в инициализатор метод repr"""
        print(repr(self))

    def __repr__(self):
        '''Method repr для вывода в инициализаторе сообщения в виде сзданного класа и его атрибутов(свойств)'''
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v},'
        return f"Создан объект со свойствами {object_attributes})"

