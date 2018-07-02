#O padrão Decorador reduz o número de variações a serem criadas
#de uma classe criando uma abstração para as diferentes opções. Ele funciona
#da seguinte forma: ao cliente é dado o poder de selecionar qual combinação
#de features ele deseja. A solução para o decorador envolve encapsular o objeto
#original em uma interface wrapper. Os objetos decoradores e core herdam dessa
#interface abstrata. Através de composição criam-se as layers para os decoradores
#que geram as diferentes opções
class Component:
    def propriedades(self):
        pass


class Decorator:
    def __init__(self, componente):
        self.componente = componente

    def propriedades(self):
        pass


class Veneno(Decorator):
    def propriedades(self):
        print(" Veneno")
        self.componente.propriedades()


class Adaga(Decorator):
    def propriedades(self):
        print("Adaga possui:")
        self.componente.propriedades()


class Lamina(Component):
    def propriedades(self):
        print(" lamina")


if __name__ == "__main__":
    lamina = Lamina()
    poison = Veneno(lamina)
    adaga = Adaga(poison)
    adaga.propriedades()