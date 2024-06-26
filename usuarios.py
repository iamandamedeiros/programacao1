import json

ARQUIVO_USUARIOS = 'usuarios.json'

def carrega_usuarios():
    try:
        with open(ARQUIVO_USUARIOS, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def salva_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, 'w') as file:
        json.dump(usuarios, file, indent=4)

def inserir_usuario(nome, email):
    usuarios = carrega_usuarios()
    usuario = {'id': len(usuarios) + 1, 'nome': nome, 'email': email}
    usuarios.append(usuario)
    salva_usuarios(usuarios)

def remover_usuario(usuario_id):
    usuarios = carrega_usuarios()
    usuarios = [usuario for usuario in usuarios if usuario['id'] != usuario_id]
    salva_usuarios(usuarios)

def atualizar_usuario(usuario_id, nome, email):
    usuarios = carrega_usuarios()
    for usuario in usuarios:
        if usuario['id'] == usuario_id:
            usuario['nome'] = nome
            usuario['email'] = email
    salva_usuarios(usuarios)

def receber_usuarios():
    return carrega_usuarios()
