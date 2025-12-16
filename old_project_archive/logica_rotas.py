rotas = {
    'index':'index.html',
    'acesso':'acesso.html',
    'acessar':'login.html',
    'cadastrar':'signup.html',
    'definir_senha':'definir_senha.html',
}

usuario_cadastrado = True

url = '/'

if url == '/' :
    print(rotas['index'])

if url == '/acesso':
    print(rotas['acessar'])

if usuario_cadastrado:
    print(rotas['acessar'])
else:
    print(rotas['cadastrar'])
    print(rotas['definir_senha'])