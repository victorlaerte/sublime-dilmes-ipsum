# coding=utf-8

import sublime
import sublime_plugin
import random
import re

class DilmesIpsumCommand(sublime_plugin.TextCommand):

    s1 = "dilma"
    s2 = "trump"

    def run(self, edit, qty=1, person='dilma'):

        #sel() returns an iterable RegionSet
        selections = self.view.sel()
        for selection in selections:

            personality = {'dilma' : [u"Eu, para ir, eu faço uma escala. Para voltar, eu faço duas, para voltar para o Brasil. Neste caso agora nós tínhamos uma discussão. Eu tinha que sair de Zurique, podia ir para Boston, ou pra Boston, até porque... vocês vão perguntar, mas é mais longe? Não é não, a Terra é curva, viu?",
                        u"É interessante que muitas vezes no Brasil, você é, como diz o povo brasileiro, muitas vezes você é criticado por ter o cachorro e, outras vezes, por não ter o mesmo cachorro. Esta é uma crítica interessante que acontece no Brasil",
                        u"E nós criamos um programa que eu queria falar para vocês, que é o Ciência sem Fronteiras. Por que eu queria falar do Ciência sem Fronteiras para vocês? É que em todas as demais... porque nós vamos fazer agora o Ciência sem Fronteiras 2. O 1 é o 100 000, mas vai ter de continuar fazendo Ciência sem Fronteiras no Brasil",
                        u"Eu dou dinheiro pra minha filha. Eu dou dinheiro pra ela viajar, então é... é... Já vivi muito sem dinheiro, já vivi muito com dinheiro. -Jornalista: Coloca esse dinheiro na poupança que a senhora ganha R$10 mil por mês. -Dilma: O que que é R$10 mil?",
                        u"A única área que eu acho, que vai exigir muita atenção nossa, e aí eu já aventei a hipótese de até criar um ministério. É na área de... Na área... Eu diria assim, como uma espécie de analogia com o que acontece na área agrícola.",
                        u"Primeiro eu queria cumprimentar os internautas. -Oi Internautas! Depois dizer que o meio ambiente é sem dúvida nenhuma uma ameaça ao desenvolvimento sustentável. E isso significa que é uma ameaça pro futuro do nosso planeta e dos nossos países. O desemprego beira 20%, ou seja, 1 em cada 4 portugueses.",
                        u"Se hoje é o dia das crianças... Ontem eu disse: o dia da criança é o dia da mãe, dos pais, das professoras, mas também é o dia dos animais, sempre que você olha uma criança, há sempre uma figura oculta, que é um cachorro atrás. O que é algo muito importante!",
                        u"Todos as descrições das pessoas são sobre a humanidade do atendimento, a pessoa pega no pulso, examina, olha com carinho. Então eu acho que vai ter outra coisa, que os médicos cubanos trouxeram pro brasil, um alto grau de humanidade.",
                        u"No meu xinélo da humildade eu gostaria muito de ver o Neymar e o Ganso. Por que eu acho que.... 11 entre 10 brasileiros gostariam. Você veja, eu já vi, parei de ver. Voltei a ver, e acho que o Neymar e o Ganso têm essa capacidade de fazer a gente olhar.",
                        u"A população ela precisa da Zona Franca de Manaus, porque na Zona franca de Manaus, não é uma zona de exportação, é uma zona para o Brasil. Portanto ela tem um objetivo, ela evita o desmatamento, que é altamente lucravito. Derrubar arvores da natureza é muito lucrativo!",
                        u"Ai você fala o seguinte: \"- Mas vocês acabaram isso?\" Vou te falar: -\"Não, está em andamento!\" Tem obras que \"vai\" durar pra depois de 2010. Agora, por isso, nós já não desenhamos, não começamos a fazer projeto do que nós \"podêmo fazê\"? 11, 12, 13, 14... Por que é que não?"
                        u"Eu queria destacar uma questão, que é uma questão que está afetando o Brasil inteiro, que é a questão da vigilância sanitária: gente, é o vírus Aedes aegypti, com as suas diferentes modalidades: chikungunya, zika vírus."],
                        'trump' : [u"teste", u"teste2"]};

            text = "";
            chose = []
            phrases = personality[person];

            from random import randint
            for i in list(range(0, qty)):

                if i > 0: text += "\n"

                r = randint(0, len(phrases) - 1)
                while r in chose: r = randint(0, len(phrases) - 1)

                text += phrases[r]
                chose.append(r)

            r1 = sublime.Region(selection.begin() - len(self.s1), selection.begin())
            r2 = sublime.Region(selection.begin() - len(self.s2), selection.begin())

            if self.view.substr(r1).lower() == 'dilma':
                self.view.erase(edit, r1)
                selection = sublime.Region(r1.begin())
            elif self.view.substr(r2).lower() == 'trump':
                self.view.erase(edit, r2)
                selection = sublime.Region(r2.begin())
            else:
                text += "\n"
                self.view.erase(edit, selection)

            # insert text before current cursor position
            self.view.insert(edit, selection.begin(), text)
