import random

def gerar_senha(tamanho=20):
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    number = '123456789'
    simbols = '@%&$'
    caracteres = string + number + simbols
    
    while True:
        senha = [random.choice(caracteres) for _ in range (tamanho)]
        
        maiscula = any(c.isupper() for c in senha)
        minuscula = any(c.islower() for c in senha)
        numero = any(c in number for c in senha)
        simbolo = any(c in simbols for c in senha)
        
        if maiscula and minuscula and numero and simbolo:
            return ''.join(senha)

senha_completa = gerar_senha()     
print('Senha: ', senha_completa)
