# Janela -> 500px
# Título -> Conversor de Moedas
# Campos de selecionar moedas de origem e destino (campos de listas) com labels, Selecione usa moeda de origem
# Botão de Converter
# Lista de Exibição com os nomes das moedas

import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis  # Importa as funções
from pegar_cotacao import pegar_cotacao_moeda

# Configura o modo de aparência e o tema
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Criar e configurar a janela principal
janela = customtkinter.CTk()
janela.geometry("500x500")

# Obter as moedas disponíveis e conversões
dic_conversoes_disponiveis = conversoes_disponiveis()
moedas_disponiveis = nomes_moedas()

# Criar botões, textos e outros elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de Moedas", font=("", 20))
texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=list(dic_conversoes_disponiveis.keys()),
                                                command=carregar_moedas_destino)
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["Selecione uma moeda de origem"])

# Função para converter moeda (a ser implementada)
def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text=f"1 {moeda_origem} = {cotacao} {moeda_destino}")

botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text="")

# Verifica se moedas_disponiveis não está vazio
if not moedas_disponiveis:
    print("Erro: a função nomes_moedas retornou um dicionário vazio ou não conseguiu ler o arquivo.")
    moedas_disponiveis = {}

# Adiciona cada moeda disponível ao frame de rolagem
for codigo_moeda, nome_moeda in moedas_disponiveis.items():
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()

# Colocar todos os elementos na tela
titulo.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=10)
texto_cotacao_moeda.pack(padx=10, pady=10)
lista_moedas.pack(padx=10, pady=10)

# Rodar a janela
janela.mainloop()
