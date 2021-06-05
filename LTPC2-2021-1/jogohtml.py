import cherrypy
import random

class ProjetoJokenpo(object):
    @cherrypy.expose
    def index(self):
        return f"""
               <!DOCTYPE html>
               <html>
               <head>
                 <link rel="stylesheet"
                         href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css">
                         <title> Jokenpo Avançado </title>
               </head>
               <body>
                   <h1>Jokenpo Expert<h1>
                   <br>
                   <a href="https://www.youtube.com/watch?v=OtzekNVWs30">Video explicativo sobre o Jokenpo Avançado</a>
                   <br>
                   <iframe width="560" height="315" src="https://www.youtube.com/embed/OtzekNVWs30" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                   <br>
                   <form method="get" action="resultado"
                       <p>Informe a seu nome:</p>
                       <input type="text" value="nome:" name="nome"/>
                       <br>
                       <p>Escolha uma jogada - Pedra, Papel, Tesoura, Lagarto ou Spock</p>
                       <button class="button is-primary is-focused" type="subimit" value=pedra name="jogada">Pedra</button>
                       <button class="button is-link is-focused" type="subimit" value=papel name="jogada" >Papel</button>
                       <button class="button is-info is-focused" type="subimit" value=tesoura name="jogada">Tesoura</button>
                       <button class="button is-success is-focused" type="subimit" value=lagarto name="jogada">Lagarto</button>
                       <button class="button is-danger is-focused" type="subimit" value=spock name="jogada">Spock</button>
                   </form>
               </body>
            </html>"""

    @cherrypy.expose
    def resultado(self, nome, jogada):
        jogada = jogada.upper()
        nome = nome.upper()
        #Define a jogada do jogador
        if jogada == "PEDRA":
            escolha = 0
        elif jogada == "PAPEL":
            escolha = 1
        elif jogada == "TESOURA":
            escolha = 2
        elif jogada == "LAGARTO":
            escolha = 3
        elif jogada == "SPOCK":
            escolha = 4

        #Define jogada do Computador
        computador_joga = random.randint(0,4)
        # Define jogada do Computador versão textp
        if computador_joga == 0 :
            computador_escolha = "PEDRA"
        elif computador_joga == 1 :
            computador_escolha = "PAPEL"
        elif computador_joga == 2 :
            computador_escolha = "TESOURA"
        elif computador_joga == 3 :
            computador_escolha = "LAGARTO"
        elif computador_joga == 4 :
            computador_escolha = "SPOCK"

        #Acontece o jogo
        if escolha == computador_joga:
            resultado = "EMPATOU!"

        elif escolha == 0:  # PEDRA
            if (computador_joga == 1) or (computador_joga == 4):
                resultado = "PERDEU"
            elif (computador_joga == 2) or (computador_joga == 3):
                resultado = "GANHOU"

        elif escolha == 1:  # PAPEL
            if (computador_joga == 2) or (computador_joga == 3):
                resultado = "PERDEU"
            elif (computador_joga == 0) or (computador_joga == 4):
                resultado = "GANHOU"

        elif escolha == 2:  # TESOURA
            if (computador_joga == 0) or (computador_joga == 4):
                resultado = "PERDEU"
            elif (computador_joga == 1) or (computador_joga == 3):
                resultado = "GANHOU"

        elif escolha == 3:  # LAGARTO
            if (computador_joga == 0) or (computador_joga == 2):
                resultado = "PERDEU"
            elif (computador_joga == 1) or (computador_joga == 4):
                resultado = "GANHOU"

        elif escolha == 4:  # SPOCK
            if (computador_joga == 1) or (computador_joga == 3):
                resultado = "PERDEU"
            elif (computador_joga == 0) or (computador_joga == 2):
                resultado = "GANHOU"



        return f"""<html>
        <head></head>
        <body>
            <p> {nome} VOCÊ {resultado}!!</p>
            <p> A SUA ESCOLHA FOI {jogada} E A DO COMPUTADOR FOI {computador_escolha}</p>
            <br>
            <a href="http://localhost:8080">Voltar</a>
        </body>
    </html>"""

if __name__ == '__main__':
    cherrypy.quickstart(ProjetoJokenpo())
