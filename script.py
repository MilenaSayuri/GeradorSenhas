import random

tamanho_str = input("Digite o tamanho da senha desejada: ")
senha = int(tamanho_str)
site = input("Digite o nome do site: ")
login = input("Digite o nome de usuario/gmail: ")

def gerar_senha(tamanho):
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

senha_completa = gerar_senha(senha)
print("Site:", site)
print("Login:", login)
print("Senha gerada:", senha_completa)

with open("senha_gerada.txt", "a") as arquivo:
    arquivo.write(f"Site: {site}\n")
    arquivo.write(f"Login: {login}\n")
    arquivo.write(f"Senha: {senha_completa}\n")
    arquivo.write("-----------------------\n")
