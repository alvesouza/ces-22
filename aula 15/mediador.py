#É um padrão de projeto usado frequentemente quando deseja-se
# encapsular como os objetos interagem, ou seja, a comunicação entre os
# objetos é estabelecida através do Mediator. Este padrão é considerado um padrão
# comportamental, pois o padrão pode alterar o comportamento da
# aplicação (programa).O Mediator promove o fraco acoplamento ao evitar que
# objetos se referiram uns aos outros explicitamente.
import random
class Ringue:#mediator
    def __init__(self,nome1,nome2):
        self.inimigo1 = Inimigo1(nome1,self)
        self.inimigo2 = Inimigo2(nome2,self)
        self.vencedor = 0
    def narraLuta(self):
        while self.inimigo1.getHp() > 0 and self.inimigo2.getHp() > 0:
            if random.randint(1,3) > 2 :
                self.inimigo2.chutar()
            else:
                self.inimigo1.socar()
        print("O vencedor é:")
        if self.vencedor == 1:
            print(self.inimigo1.nome + "!")
        if self.vencedor == 2:
            print(self.inimigo2.nome + "!")

class lutador:
    def __init__(self, nome,mediator):
        self.mediador = mediator
        self.nome = nome
        self.hp = 100


    def recebeDano(self, dano):
        self.hp -= dano

    def getHp(self):
        return self.hp

class Inimigo1(lutador):
    def socar(self):
        self.mediador.inimigo2.recebeDano(15)
        if (self.mediador.inimigo2.getHp() <= 0):
            self.mediador.vencedor = 1
        print(self.nome + " soca " +self.mediador.inimigo2.nome +
                                   " causando 15 de dano, agora "
              +self.mediador.inimigo2.nome +
              " tem " + str(self.mediador.inimigo2.getHp()) + " de HP")



class Inimigo2(lutador):
    def chutar(self):
        self.mediador.inimigo1.recebeDano(25)
        if(self.mediador.inimigo1.getHp() <= 0):
            self.mediador.vencedor = 2
        print(self.nome + " chuta " +self.mediador.inimigo1.nome +
                                   " causando 25 de dano, agora "
              +self.mediador.inimigo1.nome +
              " tem " + str(self.mediador.inimigo1.getHp()) + " de HP")


if __name__ == "__main__":
    mediator = Ringue("Anderson","Matheus")
    mediator.narraLuta()