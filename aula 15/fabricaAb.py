#O padrão Fábrica Abstrata oferece interfaces para uso e criação
#sem especificar suas classes. Ele funciona da seguinte forma: o cliente interage
#com a fábrica abstrata, a qual poderá utilizar uma de diversas implementações
#da fábrica concreta para instanciar um objeto. O cliente receberá um objeto
#abstrato da requisição dele
class FabricaAbstrata:
    def criaProdutoA(self):
        pass

    def criaProdutoB(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def criaProdutoA(self):
        return Produto1A()

    def criaProdutoB(self):
        return Produto1B()


class ConcreteFactory2(AbstractFactory):
    def criaProdutoA(self):
        return Produto2A()

    def criaProdutoB(self):
        return Produto2B()


class ProdutoAAbstrato:
    def interfaceA(self):
        pass


class Produto1A(ProdutoAAbstrato):
    def interfaceA(self):
        print("produto 1-A")


class Produto2A(ProdutoAAbstrato):
    def interfaceA(self):
        print("produto 2-A")


class ProdutoBAbstrato:
    def interfaceB(self):
        pass


class Produto1B(ProdutoBAbstrato):
    def interfaceB(self):
        print("produto 1-B")


class Produto2B(ProdutoBAbstrato):
    def interfaceB(self):
        print("produto 2-B")
