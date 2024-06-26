import json
from datetime import datetime, timedelta

ARQUIVO_EMPRESTIMOS = 'emprestimos.json'
ARQUIVO_LIVROS = 'livros.json'
ARQUIVO_USUARIOS = 'usuarios.json'

def carrega_emprestimos():
    try:
        with open(ARQUIVO_EMPRESTIMOS, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salva_emprestimos(emprestimos):
    with open(ARQUIVO_EMPRESTIMOS, 'w') as file:
        json.dump(emprestimos, file, indent=4)

def carrega_livros():
    try:
        with open(ARQUIVO_LIVROS, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salva_livros(livros):
    with open(ARQUIVO_LIVROS, 'w') as file:
        json.dump(livros, file, indent=4)

def carrega_usuarios():
    try:
        with open(ARQUIVO_USUARIOS, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def calcular_data_devolucao(data_emprestimo):
    dias_uteis = 7  
    data_devolucao = data_emprestimo
    while dias_uteis > 0:
        data_devolucao += timedelta(days=1)
        if data_devolucao.weekday() < 5:  
            dias_uteis -= 1
    return data_devolucao

def emprestar_livro(usuario_id, livro_id):
    emprestimos = carrega_emprestimos()
    livros = carrega_livros()
    usuarios = carrega_usuarios()

    for livro in livros:
        if livro['id'] == livro_id:
            if not livro['disponível']:
                return False

    emprestimos_usuario = [e for e in emprestimos if e['usuario_id'] == usuario_id and not e['devolvido']]
    if len(emprestimos_usuario) >= 3:
        return False

    data_emprestimo = datetime.now()
    data_devolucao = calcular_data_devolucao(data_emprestimo)

    novo_emprestimo = {
        'id': len(emprestimos) + 1,
        'usuario_id': usuario_id,
        'livro_id': livro_id,
        'data_emprestimo': data_emprestimo.isoformat(),
        'data_devolucao': data_devolucao.isoformat(),
        'devolvido': False
    }
    emprestimos.append(novo_emprestimo)

    for livro in livros:
        if livro['id'] == livro_id:
            livro['disponível'] = False

    salva_emprestimos(emprestimos)
    salva_livros(livros)
    return True

def devolver_livro(livro_id):
    emprestimos = carrega_emprestimos()
    livros = carrega_livros()

    for emprestimo in emprestimos:
        if emprestimo['livro_id'] == livro_id and not emprestimo['devolvido']:
            emprestimo['devolvido'] = True
            break

    for livro in livros:
        if livro['id'] == livro_id:
            livro['disponível'] = True
            break

    salva_emprestimos(emprestimos)
    salva_livros(livros)

def atualizar_emprestimo(emprestimo_id, novo_livro_id):
    emprestimos = carrega_emprestimos()
    livros = carrega_livros()

    for emprestimo in emprestimos:
        if emprestimo['id'] == emprestimo_id:
            for livro in livros:
                if livro['id'] == emprestimo['livro_id']:
                    livro['disponível'] = True
            emprestimo['livro_id'] = novo_livro_id
            for livro in livros:
                if livro['id'] == novo_livro_id:
                    livro['disponível'] = False
            break

    salva_emprestimos(emprestimos)
    salva_livros(livros)

def receber_emprestimos():
    return carrega_emprestimos()

