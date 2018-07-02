#Com o padrão State é possı́vel alterar o comportamento de um
#objeto quando o estado interno é modificado. Desse modo, cada classe estado
#tem sua implementação, mas há uma única interface para o mundo. Pode-se
#entendê-lo como uma máquina de estados OO. Ele funciona da seguinte forma:
#a interface da máquina de estados é encapsulada em uma classe wrapper. As
#classes interiores espelham o wrapper com exceção de um parâmetro, o qual
#permite comunicação entre as classes interiores o o wrapper
class Objeto:
    def __init__(self, estado):
        self.estado = estado
        self.hp = 100

    def qual_estado(self):
        self.estado.handle()
    def mudaEstado(self,estado):
        self.estado = estado
    def recebeDano(self,dano):
        self.hp -= dano
    def getHp(self):
        return self.hp


class Estado:
    def handle(self):
        pass


class morto(Estado):
    def handle(self):
        print("objeto esta morto")


class vivo(Estado):
    def handle(self):
        print("objeto esta vivo,pode atacar")


if __name__ == "__main__":
    objeto = Objeto(vivo())
    objeto.qual_estado()
    print("Hp do Objeto é " + str(objeto.getHp()))
    while(objeto.getHp() > 0):
        print("Objeto recebe dano de 15")
        objeto.recebeDano(15)
        print("Hp do Objeto é " + str(objeto.getHp()))
    objeto.mudaEstado(morto())
    objeto.qual_estado()