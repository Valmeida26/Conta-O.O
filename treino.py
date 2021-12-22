def dados_pessoais(nome, idade, peso, altura):
    dados = {"nome":nome, "idade":idade, "peso":peso, "altura":altura}
    return dados
def anos_de_vida(dados,anos):
    dados["idade"] += anos
def peso_agora(dados,kg):
    dados["peso"]+=kg
def altura_agora(dados,cm):
    dados["altura"] +=cm