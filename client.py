import pygame
from tabuleiro import Tabuleiro
from caixadochat import CaixaChat
from digitacaodotexto import TextoEntrada
from Botao import Botao
import threading
import Pyro4
import random


def procura_servidor():
    ns = Pyro4.locateNS()
    uri = ns.lookup('servidor')
    server2 = Pyro4.Proxy(uri)
    return server2


server = None
cliente = None

name = input("Digite o seu nome:")


@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class cliente():
    def __init__(self):
        self.chat = []
        self.nome = ""
        self.minhas_pecas = ""

    def get_minhas_pecas(self):
        return self.minhas_pecas

    def set_minhas_pecas(self, cor):
        self.minhas_pecas = cor

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome

    def get_chat(self):
        return self.chat

    def add_chat(self, mensagem, nome):
        self.chat.append(nome + ": " + mensagem)
        if len(self.chat) == 12:
            self.chat.pop(0)

    def reseta_partida(self):
        resetar_partida()

    def atualiza_chat(self):
        enviar_mensagem()

    def troca_jogador(self):
        de_quem_e_a_vez()

    def houve_desistencia(self, cor):
        desistiu(cor)

    def atualiza_posicao_peca(self, x1, y1, x2, y2):
        atualiza_posicao_pecas(x1, y1, x2, y2)

    def escolheu_cor(self, cor):
        if cor == "vermelho":
            botao_cor_cinza_rect = botao_cor_cinza.desenha_botao(screen, 850, 680, 100, 50)
            pygame.display.flip()
        elif cor == "preto":
            botao_cor_cinza_rect = botao_cor_cinza.desenha_botao(screen, 650, 680, 100, 50)
            pygame.display.flip()


def desistiu(cor):
    if cor == "vermelho":
        screen.fill(cinza)
        screen.blit(opretovenceu, (0, 0))
        pygame.display.flip()
    elif cor == "preto":
        screen.fill(cinza)
        screen.blit(overmelhovenceu, (0, 0))
        pygame.display.flip()

def de_quem_e_a_vez():
    global vez_de
    vez_de = server.get_vez_de()
    if vez_de == "preto":
        pygame.draw.circle(screen, preto, (175, 25), 15)
        pygame.display.flip()
    elif vez_de == "vermelho":
        pygame.draw.circle(screen, vermelho, (175, 25), 15)
        pygame.display.flip()


def atualiza_posicao_pecas(x1, y1, x2, y2):
    tabuleiro.muda_posicao_circulo(x1, y1, x2, y2)
    tabuleiro.desenha_tabuleiro(screen)
    tabuleiro.verifica_se_peca_foi_comida(x2, y2)
    tabuleiro.verifica_se_tem_ganhador()
    tabuleiro.desenha_tabuleiro(screen)
    pygame.display.flip()


def text_objects(text, font, cor):
    textSurface = font.render(text, True, cor)
    return textSurface, textSurface.get_rect()


def message_display(x, y, text, size, cor):
    largeText = pygame.font.Font('freesansbold.ttf', size)
    TextSurf, TextRect = text_objects(text, largeText, cor)
    TextRect.center = (x, y)
    pygame.display.get_surface().blit(TextSurf, TextRect)


preto = (0, 0, 0, 255)
roxo = (128, 0, 128, 255)
vermelho = (255, 0, 0, 255)
amarelo = (255, 128, 0, 255)
verde = (0, 255, 0, 255)
branco = (255, 255, 255, 255)
brancola = (255, 255, 254, 255)
cinza = (128, 128, 128, 255)
azul = (0, 0, 255, 255)
MOUSE_LEFT = 1
MOUSE_RIGHT = 3
pygame.init()
size = [1200, 800]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bizingo")
overmelhovenceu = pygame.image.load("Vitoria_do_Vermelho.jpg")
opretovenceu = pygame.image.load("Vitoria_do_Preto.jpg")
circulos = []
screen.fill(cinza)
minhas_pecas = ""
# inicializando o botao de passar turno
botao_passar_turno = Botao("Passar a vez", (128, 0, 128), roxo)
botao_passar_turno_rect = botao_passar_turno.desenha_botao(screen, 150, 550, 200, 50)
# inicializando o botao de enviar mensagens
send_mensage_button = Botao("Enviar", (255, 1, 127), brancola)
send_message_button_rect = send_mensage_button.desenha_botao(screen, 920, 490, 200, 50)
# inicializando o botao de desistir , mas nao ta funcionando ainda
botao_desistir = Botao("Desistir", (255, 51, 255), azul)
botao_desistir_rect = botao_desistir.desenha_botao(screen, 150, 650, 200, 50)
botao_cor_vermelho = Botao("", (255, 0, 0), vermelho)
botao_cor_vermelho_rect = botao_cor_vermelho.desenha_botao(screen, 650, 680, 100, 50)
botao_cor_preto = Botao("", (0, 0, 0), preto)
botao_cor_preto_rect = botao_cor_preto.desenha_botao(screen, 850, 680, 100, 50)
# inicializando a caixa do chat
caixa_chat = CaixaChat(screen, 500, 80, 600, 350, brancola)
# inicializando a caixa de entrada de texto
texto_entrada = TextoEntrada(screen, 500, 460, 400, 110, brancola, "")
input_para_caixa_do_chat = ""
botao_esconde_texto = Botao("", (128, 128, 128), cinza)
botao_cor_cinza = Botao("", (128, 128, 128), cinza)
botao_resetar_partida = Botao("Resetar partida", (0, 0, 255), preto)
vez_de = ""
botao_resetar_partida_rect = botao_resetar_partida.desenha_botao(screen, -50, -50, 1, 1)
message_display(90, 25, "Jogador atual: ", 20, (0, 0, 0, 255))
message_display(700, 650, "Para começar escolha sua cor: ", 20, (0, 0, 0, 255))
tabuleiro = Tabuleiro()
tabuleiro.desenha_tabuleiro(screen)

clock = pygame.time.Clock()
mover = True


def register_name_server_object(name):
    daemon = Pyro4.Daemon()
    uri = daemon.register(cliente)
    ns = Pyro4.locateNS()
    ns.register(name, uri)
    thread = threading.Thread(target=daemon.requestLoop)
    thread.daemon = True
    thread.start()


def verifica_dentro_do_circulo(x, y, a, b, r):
    return (x - a) * (x - a) + (y - b) * (y - b) < r * r


def enviar_mensagem():
    texto_entrada.clean_input()
    pygame.display.flip()
    caixa_chat.set_chatarray(cliente.get_chat())
    caixa_chat.atualiza_tela_chatarray()


def acao(message):
    return message.split()[0]


def sorteio():
    numero_sorteado = random.randint(0, 100)
    return numero_sorteado


def esconde_botao_vermelho():
    global botao_cor_cinza_rect, botao_esconde_texto_rect, botao_resetar_partida_rect
    botao_cor_cinza_rect = botao_cor_cinza.desenha_botao(screen, 650, 680, 100, 50)
    botao_cor_cinza_rect = botao_cor_cinza.desenha_botao(screen, 850, 680, 100, 50)
    pygame.display.flip()
    botao_esconde_texto_rect = botao_esconde_texto.desenha_botao(screen, 500, 600, 400, 100)
    botao_resetar_partida_rect = botao_resetar_partida.desenha_botao(screen, 700, 680, 200, 50)


def esconde_botao_preto():
    global botao_cor_cinza_rect, botao_esconde_texto_rect, botao_resetar_partida_rect
    botao_cor_cinza_rect = botao_cor_cinza.desenha_botao(screen, 850, 680, 100, 50)
    botao_cor_cinza_rect = botao_cor_cinza.desenha_botao(screen, 650, 680, 100, 50)
    botao_esconde_texto_rect = botao_esconde_texto.desenha_botao(screen, 500, 600, 500, 200)
    botao_resetar_partida_rect = botao_resetar_partida.desenha_botao(screen, 700, 680, 200, 50)
    pygame.display.flip()


def resetar_partida():
    tabuleiro.teste()
    caixa_chat = CaixaChat(screen, 500, 80, 600, 350, brancola)
    tabuleiro.desenha_tabuleiro(screen)
    pygame.display.flip()


def rodar():
    global circulos, input_para_caixa_do_chat, minhas_pecas, vez_de, botao_resetar_partida_rect, botao_cor_cinza_rect, botao_esconde_texto_rect, ganhador
    done = False
    vez_de = server.get_vez_de()
    if vez_de == "preto":
        pygame.draw.circle(screen, preto, (175, 25), 15)
    else:
        pygame.draw.circle(screen, vermelho, (175, 25), 15)
    while not done:
        for event in pygame.event.get():  # User did something
            try:
                caixa_chat.atualiza_tela_chatarray()
            except:
                pass
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
                server.del_player(cliente)
                if cliente.get_minhas_pecas() == "vermelho":
                    server.set_pegou_vermelho()
                if cliente.get_minhas_pecas() == "preto":
                    server.set_pegou_preto()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == MOUSE_LEFT:
                    if botao_cor_vermelho_rect.collidepoint(event.pos) and minhas_pecas != "preto":
                        minhas_pecas = "vermelho"
                        cliente.set_minhas_pecas("vermelho")
                        server.set_pegou_vermelho()
                        server.adversario_escolha_cor(cliente.get_nome(), "preto")
                        esconde_botao_vermelho()
                        message_display(150, 750, "JOGADOR VERMELHO ", 20, (255, 0, 0, 255))
                        tabuleiro.desenha_tabuleiro(screen)
                        pygame.display.flip()
                    elif botao_cor_preto_rect.collidepoint(event.pos) and minhas_pecas != "vermelho":
                        minhas_pecas = "preto"
                        cliente.set_minhas_pecas("preto")
                        server.set_pegou_preto()
                        server.adversario_escolha_cor(cliente.get_nome(), "vermelho")
                        esconde_botao_preto()
                        tabuleiro.desenha_tabuleiro(screen)
                        message_display(150, 750, "JOGADOR PRETO ", 20, (0, 0, 0, 255))
                        pygame.display.flip()
                    elif botao_resetar_partida_rect.collidepoint(event.pos):
                        resetar_partida()
                        server.adversario_resetar_partida(cliente.get_nome())
                    elif texto_entrada.get_input_text_rect().collidepoint(event.pos):
                        texto_entrada.handle_event(event)
                    elif send_message_button_rect.collidepoint(event.pos):
                        cliente.add_chat(input_para_caixa_do_chat, cliente.get_nome())
                        server.adversario_adiciona_mensagem(input_para_caixa_do_chat, cliente.get_nome())
                        input_para_caixa_do_chat = ""
                        enviar_mensagem()
                    elif botao_passar_turno_rect.collidepoint(event.pos):
                        if vez_de == "vermelho" and minhas_pecas == "vermelho":
                            vez_de = "preto"
                            pygame.draw.circle(screen, preto, (175, 25), 15)
                            server.troca_jogador()
                            server.adversario_troca_jogador(cliente.get_nome())
                            pygame.display.flip()
                        elif vez_de == "preto" and minhas_pecas == "preto":
                            vez_de = "vermelho"
                            server.troca_jogador()
                            server.adversario_troca_jogador(cliente.get_nome())
                            pygame.draw.circle(screen, vermelho, (175, 25), 15)
                            pygame.display.flip()
                    elif botao_desistir_rect.collidepoint(event.pos):
                        if minhas_pecas == "vermelho":
                            ganhador = "preto"
                            screen.fill(cinza)
                            screen.blit(opretovenceu, (0, 0))
                            server.adversario_ganhou_partida_desistencia(cliente.get_nome(), "vermelho")
                            pygame.display.flip()
                        elif minhas_pecas == "preto":
                            ganhador = "vermelho"
                            server.adversario_ganhou_partida_desistencia(cliente.get_nome(), "preto")
                            screen.fill(cinza)
                            screen.blit(overmelhovenceu, (0, 0))
                            pygame.display.flip()
                    position_mouse = pygame.mouse.get_pos()
                    color = screen.get_at(pygame.mouse.get_pos())
                    x_da_peca = position_mouse[0]
                    y_da_peca = position_mouse[1]
                    if len(circulos) < 2 and vez_de == minhas_pecas:
                        circulo = tabuleiro.verifica_se_e_bola(x_da_peca, y_da_peca)
                        if len(circulos) == 0 and circulo is not None:
                            circulos.append(circulo)
                        elif len(circulos) == 1 and (
                                (circulos[0].get_cor() == amarelo or circulos[
                                    0].get_cor() == vermelho) and color == branco and minhas_pecas == "vermelho"):
                            x_desejada = position_mouse[0]
                            y_desejado = position_mouse[1]
                            x_da_peca, y_da_peca = circulos[0].get_x_y()
                            tabuleiro.muda_posicao_circulo(x_da_peca, y_da_peca, x_desejada, y_desejado)
                            server.adversario_muda_posicao_circulo(cliente.get_nome(), x_da_peca, y_da_peca, x_desejada,
                                                                   y_desejado)
                            tabuleiro.desenha_tabuleiro(screen)
                            pygame.display.flip()
                            tabuleiro.verifica_se_peca_foi_comida(x_desejada, y_desejado)
                            tabuleiro.verifica_se_tem_ganhador()
                            tabuleiro.desenha_tabuleiro(screen)
                            pygame.display.flip()
                            circulos = []
                        elif len(circulos) == 1 and (
                                (circulos[0].get_cor() == preto or circulos[
                                    0].get_cor() == roxo) and color == verde and minhas_pecas == "preto"):
                            x_desejada = position_mouse[0]
                            y_desejado = position_mouse[1]
                            x_da_peca, y_da_peca = circulos[0].get_x_y()
                            tabuleiro.muda_posicao_circulo(x_da_peca, y_da_peca, x_desejada, y_desejado)
                            server.adversario_muda_posicao_circulo(cliente.get_nome(), x_da_peca, y_da_peca, x_desejada,y_desejado)
                            tabuleiro.desenha_tabuleiro(screen)
                            pygame.display.flip()
                            tabuleiro.verifica_se_peca_foi_comida(x_desejada, y_desejado)
                            tabuleiro.verifica_se_tem_ganhador()
                            tabuleiro.desenha_tabuleiro(screen)
                            pygame.display.flip()
                            circulos = []
                        else:
                            circulos = []
            if event.type == pygame.KEYDOWN:
                texto_entrada.handle_event(event)
                input_para_caixa_do_chat = texto_entrada.draw(screen)
                pygame.display.flip()


# Be IDLE friendly
def localizar_cliente(nome):
    ns = Pyro4.locateNS()
    uri = ns.lookup(nome)
    return Pyro4.Proxy(uri)


if __name__ == "__main__":
    pygame.init()
    server = procura_servidor()
    register_name_server_object(name)
    cliente = localizar_cliente(name)
    cliente.set_nome(name)
    server.add_player(cliente)
    print(cliente.get_nome())
    rodar()
    pygame.quit()
    pygame.quit()
