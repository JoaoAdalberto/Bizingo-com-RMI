import Pyro4


@Pyro4.expose  # Disponibiliza o acesso remoto
@Pyro4.behavior(instance_mode="single")
class Servidor():
    def __init__(self):
        self.lista_players = []

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