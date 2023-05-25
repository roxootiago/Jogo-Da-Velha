class JogoDaVelha:
    tabuleiro = []

    for i in range(-1, 8):
        tabuleiro.append(i + 1)

    def __init__(self, inicialPlayer="X"):
        self.turno = inicialPlayer

    def ImprimirTab(self):
        print("┌───┬───┬───┐")
        print(f"| {self.tabuleiro[0]} | {self.tabuleiro[1]} | {self.tabuleiro[2]} |")
        print("├───┼───┼───┤")
        print(f"| {self.tabuleiro[3]} | {self.tabuleiro[4]} | {self.tabuleiro[5]} |")
        print("├───┼───┼───┤")
        print(f"| {self.tabuleiro[6]} | {self.tabuleiro[7]} | {self.tabuleiro[8]} |")
        print("└───┴───┴───┘")

    def Win(self):
        if self.tabuleiro[0] == self.tabuleiro[3] == self.tabuleiro[6]:
            return True
        elif self.tabuleiro[1] == self.tabuleiro[4] == self.tabuleiro[5]:
            return True
        elif self.tabuleiro[2] == self.tabuleiro[5] == self.tabuleiro[8]:
            return True

        elif self.tabuleiro[0] == self.tabuleiro[1] == self.tabuleiro[2]:
            return True
        elif self.tabuleiro[3] == self.tabuleiro[4] == self.tabuleiro[5]:
            return True
        elif self.tabuleiro[6] == self.tabuleiro[7] == self.tabuleiro[8]:
            return True

        elif self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8]:
            return True
        elif self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6]:
            return True

    def jogar(self):

        while True:
            print(f"Jogada de {self.turno}")
            self.ImprimirTab()
            print(self.tabuleiro)
            chute = int(input("Digite uma posição: "))

            for x in range(len(self.tabuleiro)):
                if chute == self.tabuleiro[x]:
                    self.tabuleiro[x] = self.turno

            if self.Win():
                print(f"Parabéns! {self.turno} venceu")
                break

            if self.turno == "X":
                self.turno = "O"
            else:
                self.turno = "X"

        self.ImprimirTab()


jogo = JogoDaVelha()
jogo.jogar()
