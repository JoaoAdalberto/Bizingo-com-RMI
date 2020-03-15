import Pyro4
import random


def sorteio():
    numero_sorteado = random.randint(0, 100)
    if numero_sorteado > 50:
        return "vermelho"
    elif numero_sorteado < 50:
        return "preto"


@Pyro4.expose  # Disponibiliza o acesso remoto
@Pyro4.behavior(instance_mode="single")
class Servidor():
    def __init__(self):
        self.lista_players = []
        self.vez_de = sorteio()
        self.pegou_vermelho = False
        self.pegou_preto = False

    def get_vez_de(self):
        return self.vez_de

    def troca_jogador(self):
        if self.vez_de == "preto":
            self.vez_de = "vermelho"
        elif self.vez_de == "vermelho":
            self.vez_de = "preto"

    def adversario_ganhou_partida_desistencia(self, remetente, cor):
        for player in self.lista_players:
            nome = player.get_nome()
            if nome != remetente:
                player.houve_desistencia(cor)

    def adversario_resetar_partida(self, remetente):
        for player in self.lista_players:
            nome = player.get_nome()
            if nome != remetente:
                player.reseta_partida()

    def adversario_troca_jogador(self, remetente):
        for player in self.lista_players:
            nome = player.get_nome()
            if nome != remetente:
                player.troca_jogador()

    def adversario_muda_posicao_circulo(self, remetente, x1, y1, x2, y2):
        for player in self.lista_players:
            if player.get_nome() != remetente:
                player.atualiza_posicao_peca(x1, y1, x2, y2)

    def adversario_escolha_cor(self, remetente, cor_adversario):
        for player in self.lista_players:
            nome = player.get_nome()
            if nome != remetente:
                player.escolheu_cor(cor_adversario)

    def get_pegou_vermelho(self):
        return self.pegou_vermelho

    def get_pegou_preto(self):
        return self.pegou_preto

    def set_pegou_vermelho(self):
        if not self.pegou_vermelho:
            self.pegou_vermelho = True
        elif self.pegou_vermelho:
            self.pegou_vermelho = False

    def set_pegou_preto(self):
        if not self.pegou_preto:
            self.pegou_preto = True
        elif self.pegou_preto:
            self.pegou_preto = False

    def add_player(self, cliente):
        self.lista_players.append(cliente)
        print(self.lista_players)

    def del_player(self, cliente):
        ns = Pyro4.locateNS()
        ns.remove(cliente.get_nome())
        self.lista_players.remove(cliente)
        print(self.lista_players)

    def adversario_adiciona_mensagem(self, mensagem, remetente):
        for player in self.lista_players:
            nome = player.get_nome()
            if nome != remetente:
                player.add_chat(mensagem, remetente)
                player.atualiza_chat()


def return_obj_name_server(uri):
    return Pyro4.Proxy(uri)


def main():
    daemon = Pyro4.Daemon()  # make a Pyro daemon
    uri = daemon.register(Servidor)  # registra o servidor como um objeto pyro
    ns = Pyro4.locateNS()
    ns.register("servidor", uri)
    print(uri)
    daemon.requestLoop()  # Começa o loop de esperar chamadas


if __name__ == "__main__":
    main()
