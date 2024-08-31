import xmltodict

def nomes_moedas():
    try:
        with open("moedas.xml", "rb") as arquivo_moedas:
            dic_moedas = xmltodict.parse(arquivo_moedas)
            moedas = dic_moedas.get("xml", {})
            return moedas
    except Exception as e:
        print(f"Erro ao ler moedas.xml: {e}")
        return {}

def conversoes_disponiveis():
    try:
        with open("conversoes.xml", "rb") as arquivo_conversoes:
            dic_conversoes = xmltodict.parse(arquivo_conversoes)
            conversoes = dic_conversoes.get("xml", [])
            dic_conversoes_disponiveis = {}
            for par_conversao in conversoes:
                # Supondo que cada item em conversoes seja uma string no formato "moeda_origem-moeda_destino"
                moeda_origem, moeda_destino = par_conversao.split("-")
                if moeda_origem in dic_conversoes_disponiveis:
                    dic_conversoes_disponiveis[moeda_origem].append(moeda_destino)
                else:
                    dic_conversoes_disponiveis[moeda_origem] = [moeda_destino]
            return dic_conversoes_disponiveis
    except Exception as e:
        print(f"Erro ao ler conversoes.xml: {e}")
        return {}

# Testar a função conversoes_disponiveis (remover ou comentar em produção)
if __name__ == "__main__":
    conversoes = conversoes_disponiveis()
    print(conversoes)