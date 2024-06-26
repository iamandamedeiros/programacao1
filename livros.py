import json

ARQUIVO_LIVROS = 'livros.json'

def carrega_livros():
    try:
        with open(ARQUIVO_LIVROS, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salva_livros(livros):
    with open(ARQUIVO_LIVROS, 'w') as file:
        json.dump(livros, file, indent=4)

def inserir_livro(titulo, autor):
    livros = carrega_livros()
    livro = {'id': len(livros) + 1, 'titulo': titulo, 'autor': autor, 'disponivel': True}
    livros.append(livro)
    salva_livros(livros)

def remover_livro(livro_id):
    livros = carrega_livros()
    livros = [livro for livro in livros if livro['id'] != livro_id]
    salva_livros(livros)

def atualizar_livro(livro_id, titulo, autor):
    livros = carrega_livros()
    for livro in livros:
        if livro['id'] == livro_id:
            livro['titulo'] = titulo
            livro['autor'] = autor
    salva_livros(livros)

def receber_livros():
    return carrega_livros()
