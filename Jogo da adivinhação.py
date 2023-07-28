# Importar a biblioteca tkinter e renomeá-la para "tk"
import tkinter as tk
from random import randint

cont_geral = 0

while cont_geral == 0:
    cont = numero_pc = cont_vitoria = 0
    if cont_geral > 0:
        break
    print(cont_geral)
    # Definir a função "exibir_mensagem"
    def exibir_mensagem():
        # Destruir o botão "Iniciar jogo" para removê-lo da interface gráfica
        botao_iniciar.destroy()

        # Definir a função "exibir_texto_digitado"
        def exibir_texto_digitado():
            #verificação para o usuario só usar o botao duas vezes
            global cont, cont_vitoria
            numero_pc = randint(1, 10)
            cont+= 1
            if cont >= 3:
                def encerrar_sim_nao():
                    def sim_button_click():
                        global janela, cont_geral
                        def encerrar_jogo():
                            botao.destroy()
                            campo_entrada.destroy()
                            janela.destroy()
                        print("Você clicou em SIM!")
                        cont_geral = 0
                        print(cont_geral)
                        encerrar_jogo()
                        janela.quit()

                    def nao_button_click():
                        global janela, cont_geral
                        print("Você clicou em NÃO!")
                        cont_geral = 1
                        print(cont_geral)
                        janela.quit()

                    # Criar botão "SIM"
                    botao_sim = tk.Button(janela, text="SIM", command=sim_button_click, width=20, foreground="green")
                    botao_sim.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

                    # Criar botão "NÃO"
                    botao_nao = tk.Button(janela, text="NÃO", command=nao_button_click, width=20, foreground="red")
                    botao_nao.place(relx=0.7, rely=0.4, anchor=tk.CENTER)
                botao.destroy()
                campo_entrada.destroy()
                label["text"] = "Jogo encerrado"
                if cont_vitoria == 0:
                    label["text"] = "VOCÊ GANHOU O JOGO\n" \
                                        "Você quer jogar novamente?"
                    encerrar_sim_nao()
                else:
                    label["text"] = "A MÁQUINA É BRABA\n" \
                                        "Você quer jogar novamente?"
                    encerrar_sim_nao()
            elif cont < 3:
                # Obter o texto digitado pelo usuário na caixa de entrada
                texto_digitado = campo_entrada.get()
                # if int(texto_digitado) == 0 or int(texto_digitado) > 10 or
                def encerrar_caso_letra_ou_maior10():
                        botao.destroy()
                        campo_entrada.destroy()
                        janela.destroy()
                if int(texto_digitado) != numero_pc and int(texto_digitado) < 10:

                    # Atualizar o texto do rótulo (label) com o texto digitado
                    label["text"] = (f"Você escolheu: {texto_digitado} "
                                         f"a Máquina escolheu: {numero_pc}\n"
                                         f"A Máquina perdeu!!")
                elif int(texto_digitado) == numero_pc:
                    cont_vitoria = 1
                    label["text"] = (f"Você Perdeu!!\n"
                                         f"A Máquina acertou seu número\n"
                                         f"Maquina escolheu: {numero_pc} e você: {texto_digitado}")
                    cont = 5
                else:
                    global cont_geral
                    cont_geral = 5
                    encerrar_caso_letra_ou_maior10()
            # print(cont)

        # Definir o texto inicial do rótulo (label) e exibi-lo na janela
        label["text"] = "Jogo da adivinhação\n" \
                            " \n" \
                            "Digite um número de 0 a 10 e clique em OK:"

        # Criar uma caixa de entrada de texto (widget Entry) e exibi-la na janela
        campo_entrada = tk.Entry(janela)
        campo_entrada.pack()

        # Criar um botão com o texto "OK" e associar a função "exibir_texto_digitado" a ele
        botao = tk.Button(janela, text="OK", command=exibir_texto_digitado)
        botao.pack()
    # Criar a janela principal
    janela = tk.Tk()

    # Definir o título da janela
    janela.title("...")

    # Configurar a janela para tela cheia
    janela.geometry("800x600")

    # Criar um rótulo (label) com o texto "Jogo da adivinhação!" e exibi-lo na janela
    label = tk.Label(janela, text=f"Jogo da adivinhação!", font=("Arial", 24), foreground="blue")
    label.pack()

    # Criar um botão com o texto "Iniciar jogo" e associar a função "exibir_mensagem" a ele
    botao_iniciar = tk.Button(janela, text="Iniciar jogo", command=exibir_mensagem)
    botao_iniciar.pack()

    # Iniciar o loop principal da interface gráfica
    janela.mainloop()
