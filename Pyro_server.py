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
        if self.vez_de == "vermelho":
            self.vez_de = "preto"
        elif self.vez_de == "preto":
            self.vez_de = "vermelho"

    def get_pegou_vermelho(self):
        return self.pegou_vermelho

    def get_pegou_preto(self):
        return self.pegou_vermelho

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