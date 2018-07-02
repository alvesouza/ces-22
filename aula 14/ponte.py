#O padrão Bridge torna possı́vel que uma abstração tenha diferentes
# implementações. Ele funciona da seguinte forma: o cliente interage com
#uma abstração e a ponte torna possı́vel que se selecione a implementação para
#a abstração desejada

class Ponte:
    def __init__(self, concreta):
        self._concreta = concreta

    def ID(self):
        self._concreta.ID()


class SerVivo:
    def ID(self):
        pass


class Cachorro(SerVivo):
    def ID(self):
        print("É um cachorro")


class Gato(SerVivo):
    def ID(self):
        print("É um gato")


if __name__ == "__main__":
    dog = Cachorro()
    ponte = Ponte(dog)
    ponte.ID()