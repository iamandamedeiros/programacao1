import json
from livros import receber_livros
from usuarios import receber_usuarios
from emprestimos import receber_emprestimos

def gerar_relatorio():
    livros = receber_livros()
    usuarios = receber_usuarios()
    emprestimos = receber_emprestimos()
    relatorio = {
        'livros': livros,
        'usuarios': usuarios,
        'emprestimos': emprestimos
    }
    arquivo_relatorio = 'relatorio.json'
    with open(arquivo_relatorio, 'w') as file:
        json.dump(relatorio, file, indent=4)
    return arquivo_relatorio
