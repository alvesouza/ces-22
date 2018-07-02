#Entende-se por Composite um padrão de projeto de software utilizado
# para representar um objeto formado pela composição de objetos similares.
# Este conjunto de objetos pressupõe uma mesma hierarquia de classes a que
# ele pertence. Tal padrão é, normalmente, utilizado para representar listas
# recorrentes - ou recursivas - de elementos. Além disso, este modo de
# representação hierárquica de classes permite que os elementos contidos em um
# objeto composto sejam tratados como se fossem um objeto único. Desta forma, os
# métodos comuns às classes podem ser aplicados, também, ao conjunto agrupado no
# objeto composto.

class SerVivo:
    def ID(self):
        pass

class Carrocinha(SerVivo):
    def __init__(self):
        self.filho = set()

    def ID(self):
        print("Os animais na carrocinha")
        for child in self.filho:
            child.ID()

    def adicionar(self, ser):
        self.filho.add(ser)

    def remover(self, ser):
        self.filho.discard(ser)


class Cachorro(SerVivo):
    def __init__(self,nome):
        self.nome = nome
    def ID(self):
        print(self.nome + " é um cachorro")


class Gato(SerVivo):
    def __init__(self,nome):
        self.nome = nome
    def ID(self):
        print(self.nome + " é um gato")


if __name__ == "__main__":
    cat = Gato("Alfred")
    car = Carrocinha()
    dog = Cachorro("Doggy")
    car.adicionar(cat)
    car.adicionar(dog)
    car.ID()